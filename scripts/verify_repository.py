"""Verify the review package and finite data without invoking Lake or Lean."""
from pathlib import Path
import hashlib,zipfile,sys,json,subprocess,tempfile,re
root=Path(__file__).resolve().parents[1]
def sha(data):return hashlib.sha256(data).hexdigest()
def run():
 subprocess.run([sys.executable, "-B", str(root/"scripts/check_text_encoding.py")], capture_output=True, encoding="utf-8", check=True)
 manifest=root/'manifest_sha256.txt'
 if manifest.exists():
  for row in manifest.read_text(encoding="utf8").splitlines():
   h,n=row.split("  ",1);assert sha((root/n).read_bytes())==h,n
 zp=next((root/"archives").glob("*.zip"));assert sha(zp.read_bytes())==zp.with_suffix(".zip.sha256").read_text(encoding='utf-8').split()[0]
 with zipfile.ZipFile(zp) as z:
  rows=z.read("SOURCE_SHA256SUMS.txt").decode().splitlines()
  assert len(rows)+1==len(z.namelist())
  for row in rows:
   h,p=row.split("  ",1);assert sha(z.read(p))==h,p
  packages=json.loads(z.read("lake-manifest.json"))['packages']
  for pkg in packages:
   if pkg['type']=='path':
    assert pkg['dir'].startswith('vendor/') and pkg['dir']+'/'+pkg['configFile'] in z.namelist()
   else:assert re.fullmatch(r'[a-f0-9]{40}',pkg['rev'])
  with tempfile.TemporaryDirectory() as temp:
   dest=Path(temp)
   for n in z.namelist():
    if n.startswith(("CDRBicolour/Base/Data/","CDRBicolour/Absorption/Exact/Trade.lean","docs/AXIOMS_6_7_20261105.txt")):
     f=dest/n;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(z.read(n))
   proc=subprocess.run([sys.executable,'-B',str(root/'scripts/check_examples.py'),str(dest)],capture_output=True,encoding='utf8')
   if proc.returncode:raise RuntimeError(proc.stderr)
   check=json.loads(proc.stdout)
 assert check['status']=='PASS' and check['witness_pairs_verified']==1203132
 for p in (root/'preprints').glob('PAPER_*'):
  for j in (p/'02_validation').glob('*_build.json'):
   data=json.loads(j.read_bytes());stem=j.stem.removesuffix('_build')
   for ext in ('md','tex','pdf'):
    f=p/('05_formalization' if stem.startswith('companion') else '01_manuscript')/(stem+'.'+ext)
    assert sha(f.read_bytes())==data[ext],f
   assert not data['layout_issues']
 return {'status':'PASS','finite_and_axiom_checks':check,'archive_files':len(rows),'clean_build_performed':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
