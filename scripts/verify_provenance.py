"""Compare the bundled Lean sources with the released Paper III zip and original counting checkout."""
from pathlib import Path
import sys,re,json,zipfile,hashlib
root=Path(__file__).resolve().parents[1]
def stripped(b):
    # Remove block documentation before comparing lines; tolerate only INSERTED resource options.
    depth=0
    for line in b.decode("utf-8-sig").splitlines():
        row=""
        for word in re.split(r"(/-|-/)",line):
            if word=="/-": depth+=1
            elif word=="-/" and depth: depth-=1
            elif depth==0: row+=word
        if row.strip(): yield row
    assert not depth
def verify(public_zip,counting):
    rec=json.loads((root/"archives/SOURCE_PROVENANCE.json").read_text(encoding='utf-8'))
    h=lambda b:hashlib.sha256(b).hexdigest()
    assert h(public_zip.read_bytes())==rec["paper_iii_archive_sha256"]
    with zipfile.ZipFile(public_zip) as upstream, zipfile.ZipFile(next((root/"archives").glob("*.zip"))) as review:
        for path,(old,new) in rec["paper_iii"].items():
            a=upstream.read(path); b=review.read("vendor/physical-typed-absorption/"+path)
            assert (h(a),h(b))==(old,new)
            original=list(stripped(a));i=0
            for line in stripped(b):
                if i<len(original) and line==original[i]: i+=1
                else: assert re.fullmatch(r"set_option (maxHeartbeats|maxRecDepth) \d+\s*(?:--.*)?",line),path
            assert i==len(original),path
        for path,(old,new) in rec["counting"].items():
            a=(counting/path.replace("CountingCone/","RequestProject/",1)).read_bytes()
            b=review.read("vendor/counting-sts-cone/"+path)
            assert (h(a),h(b))==(old,new)
            expected=[l.replace("RequestProject.","CountingCone.") if re.match(r"\s*(public\s+)?(meta\s+)?import\s+",l) else l for l in a.decode("utf-8-sig").splitlines()]
            assert expected==b.decode("utf-8-sig").splitlines(),path
    assert len(rec["paper_iii"])==999 and len(rec["counting"])==27
    print("PASS: 999 Paper III sources and 27 counting sources")
if __name__=="__main__":verify(Path(sys.argv[1]),Path(sys.argv[2]))
