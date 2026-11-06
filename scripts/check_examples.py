"""Independently read the two trade rows, the finite grid and every paired witness."""
from collections import Counter
from itertools import combinations, permutations
from math import isqrt
from pathlib import Path
import sys
import json
import re

here = Path(__file__).resolve().parent
root = here.parent
repo = Path(sys.argv[1])
def paper(doc, lang):
    n="I" if doc=="spectrum" else "II"
    return root/"preprints"/("PAPER_"+n)/"01_manuscript"/f"{doc}_{lang}.md"
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
digits = {c: i for i, c in enumerate(alphabet)}

def trade_rows():
    reference = (repo / "CDRBicolour/Absorption/Exact/Trade.lean").read_text(encoding="utf8")
    expected = []
    for name in ("T0m", "T1m"):
        body = reference.split("def " + name + " :", 1)[1].split(":=", 1)[1].split("\n\n", 1)[0]
        expected.append(["".join(t) for t in re.findall(r"\{(\d), (\d), (\d)\}", body)])
    for lang in ("en", "es"):
        paper_text = paper("spectrum",lang).read_text(encoding="utf8")
        rows = [re.findall(r"\b\d{3}\b", row) for row in paper_text.splitlines()
                if re.match(r"^\| (Low|High|Baja|Alta) \|", row)]
        assert rows == expected
    edges = []
    for count, row in enumerate(expected, 1):
        triangles = [tuple(map(int, word)) for word in row]
        assert all(len({i//3 for i in t}) == 2 for t in triangles)
        assert sum(sorted(i//3 for i in t) == [0,0,2] for t in triangles) == count
        edges.append({e for t in triangles for e in combinations(t,2)})
    assert len(edges[0]) == 27 and edges[0] == edges[1]
    return len(edges[0])

def prime(n):
    return n >= 2 and all(n % p for p in range(2,isqrt(n)+1))

def master(a,b,c,num,den):
    if c%2 or not a<c or b-a<3 or (b-a)%2!=1:
        return False
    h = a-2*(a*(a-1)//2//b)
    return 6*(c-a-1)<=c and num*c<=den*a and 6*h<=b and b+5<=h+c

def route(profile):
    a,b,c = profile
    n = sum(profile)
    p = isqrt(n)
    if n>49 and not prime(n) and not (p*p==n and prime(p) and p%3==2):
        return "descent"
    if any(master(*roles,6,7) for roles in permutations(profile)):
        return "equitable"
    cyclic = c%2==0 and b==a+1 and b+2<=c and n>=508 and 6*c<=7*a
    four = c%2 and b==a+4 and c-b>=17
    two = c%2 and b==a+2 and (c-b)%6==3 and c-b>=27
    if cyclic: return "cyclic"
    if four: return "gap_four"
    if two: return "gap_two"
    return "table"

def read_table(path, profile):
    a,b,c = profile
    n = a+b+c
    s = re.search(r'"([0-9A-Za-z+/]+)"\.toUTF8',path.read_text(encoding="utf8"))[1]
    assert len(s) == n*(n-1)
    colors = [0]*a+[1]*b+[2]*c
    table = [list(range(n)) for _ in range(n)]
    i = 0
    for x,y in combinations(range(n),2):
        z = digits[s[i]]*64+digits[s[i+1]]
        assert 0<=z<n and z!=x and z!=y
        assert len({colors[x],colors[y],colors[z]})==2
        table[x][y]=table[y][x]=z
        i+=2
    for x,y in combinations(range(n),2):
        z=table[x][y]
        assert table[x][z]==y and table[y][z]==x
    if profile==(1,2,4):
        triples=sorted({tuple(sorted((x,y,table[x][y]))) for x,y in combinations(range(n),2)})
        printed=",".join("".join(map(str,triple)) for triple in triples)
        for lang in ("en","es"):
            assert "$"+printed+"$" in (root/"preprints/PAPER_I/05_formalization"/f"companion_{lang}.md").read_text(encoding="utf8")
    return n*(n-1)//2

def main():
    profiles = set()
    for x in range(72):
        for y in range(72):
            n=x*x+x*y+y*y
            a, rem=divmod(n-2*x-y,3)
            profile=(a,a+x,a+x+y)
            if not rem and a>0 and n<5059 and n%6 in (1,3) and profile!=(2,2,5):
                profiles.add(profile)
    import csv
    grid_path = root/"preprints/PAPER_II/02_validation/finite_grid.csv"
    with grid_path.open(encoding="utf8", newline="") as grid_file:
        grid = list(csv.DictReader(grid_file))
    assert len(grid) == len(profiles)
    seen = set()
    cyclic_orders = []
    for row in grid:
        a, b, c = (int(row[key]) for key in ("a","b","c"))
        profile = (a,b,c)
        assert profile not in seen
        seen.add(profile)
        assert (int(row["order"]), int(row["x"]), int(row["y"])) == (sum(profile), b-a, c-b)
        assert row["route"] == route(profile)
        if row["route"] == "cyclic":
            assert b == a+1 and c%2 == 0 and a >= 4 and a+4 <= c
            assert 6*(c-a-1) <= c and 6*c <= 7*a
            cyclic_orders.append(sum(profile))
        if row["route"] == "gap_four":
            assert c-b >= 17
    assert seen == profiles
    assert sorted(cyclic_orders) == [1483,1723,2551,3541,3907]
    assert route((696,702,745)) == "equitable"
    routes=Counter(route(p) for p in profiles)
    expected_rows=[routes[k] for k in ("descent","equitable","cyclic","gap_four","gap_two","table")]
    for lang in ("en","es"):
        text=paper("profiles",lang).read_text(encoding="utf8")
        rows=[int(x) for x in re.findall(r"^\|[^|\n]+\| (\d+) \|$",text,re.M)]
        assert rows==expected_rows
    current={p for p in profiles if route(p)=="table"}
    paths={tuple(map(int,p.stem[2:].split("_"))):p for p in (repo/"CDRBicolour/Base/Data").glob("W_*.lean")}
    assert current==paths.keys() and len(current)==49 and len(profiles)==1551
    assert max(map(sum,current))==487
    pairs=sum(read_table(path,p) for p,path in paths.items())
    recorded=(repo/"docs/AXIOMS_6_7_20261105.txt").read_text(encoding="utf8")
    def report(text):
        return {m[1]: {s.strip() for s in m[2].split(",")} for m in
                re.finditer(r"'([^']+)' depends on axioms: \[([^\]]+)\]",text)}
    standard={"propext","Classical.choice","Quot.sound"}
    live=report((root/"publication/audit/live_axioms.txt").read_text(encoding="utf8"))
    assert len(live)==12 and live==report(recorded)
    for target,axioms in live.items():
        if ".Absorption." in target:
            assert axioms==standard
        else:
            assert standard<=axioms
            natives=axioms-standard
            assert len(natives)==49 and {tuple(map(int,re.fullmatch(
                r"CDRBicolour\.Base\.Data\.realises_(\d+)_(\d+)_(\d+)\._native\.native_decide\.ax_1_1✝",s
            ).groups())) for s in natives}==current
    print(json.dumps(dict(sorted_profiles=len(profiles), routes=dict(sorted(routes.items())),
                          witnesses=len(current),largest_order=max(map(sum,current)),
                          witness_pairs_verified=pairs,trade_edges=trade_rows(),
                          audited_declarations=len(live),status="PASS"),indent=2))

if __name__=="__main__":
    main()
