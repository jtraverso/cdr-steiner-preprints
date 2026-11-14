"""Verify Paper III release bytes and source-bound evidence; no Lean rebuild."""
from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).resolve().parents[1];P=R/'preprints/PAPER_III';V=P/'02_validation/v1.0'
def sha(b):return hashlib.sha256(b).hexdigest()
def check():
 a=json.loads((V/'AUDIT_RESULT.json').read_text(encoding='utf-8'));assert a['status']=='PASS_SCOPED_INTERNAL_AUDIT'
 for d in a['documents']:
  f=R/d['source']
  for ext,key in [('md','md_sha256'),('tex','tex_sha256'),('pdf','pdf_sha256')]:assert sha(f.with_suffix('.'+ext).read_bytes())==d[key],str(f)
 b=json.loads((V/'BILINGUAL_PARITY.json').read_text(encoding='utf-8'));assert b['status']=='PASS'
 c=json.loads((V/'CLEAN_REBUILD_AUDIT.json').read_text(encoding='utf-8'));assert c['status']=='PASS_CLEAN_RECONSTRUCTION'
 assert len(c['endpoint_axioms'])==4 and c['lean_proof_sources_unchanged']
 for value in c['endpoint_axioms'].values():assert set(value.replace('\n',' ').replace(',',' ').split())=={'propext','Classical.choice','Quot.sound'}
 for n,h in c['run_evidence_hashes'].items():assert sha((V/'clean_run'/n).read_bytes())==h,n
 f=json.loads((V/'FREEZE.json').read_text(encoding='utf-8'));zpath=R/f['archive'];assert sha(zpath.read_bytes())==f['archive_sha256']
 with zipfile.ZipFile(zpath) as z:
  assert z.testzip() is None
  for line in z.read('SHA256SUMS.txt').decode('utf-8').splitlines():
   h,n=line.split('  ',1);assert sha(z.read(n))==h,n
  source=json.loads(z.read('evidence/SOURCE_MAP.json'))
  assert len(source['modules'])==1305
  for row in source['modules']:assert sha(z.read(row['path']))==row['sha256'],row['module']
 for n,h in json.loads((P/'04_integrity/MANIFEST.json').read_text(encoding='utf-8')).items():assert sha((P/n).read_bytes())==h,n
 assert not any(x.name in {'v0.3','v0.4','v0.5'} for x in P.rglob('*'))
 return {'status':'PASS','version':'1.0','documents':4,'compiled_project_modules':1306,'standard_axiom_endpoints':4,'source_archive_sha256':f['archive_sha256'],'scope':'Release bytes, bilingual records, original clean-build evidence and complete source archive; no new Lean rebuild or peer review'}
if __name__=='__main__':print(json.dumps(check(),indent=2))
