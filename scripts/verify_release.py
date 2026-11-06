"""Read-only release checks. No Lean, network, PDF regeneration or audit-record mutation."""
from pathlib import Path
import hashlib,json,re,zipfile,subprocess,sys
R=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def check():
 subprocess.run([sys.executable, "-B", str(R/"scripts/check_text_encoding.py")], capture_output=True, encoding="utf-8", check=True)
 subprocess.run([sys.executable, "-B", str(R/"scripts/verify_intersection_evidence.py")], capture_output=True, encoding="utf-8", check=True)
 idx=json.loads((R/'PUBLICATION_INDEX.json').read_text(encoding='utf-8'));assert idx['edition']=='1.0'
 joint=json.loads((R/'publication/JOINT_DOCUMENT_AUDIT.json').read_text(encoding='utf-8'));assert joint['status']=='PASS_INTERNAL_RELEASE_AUDIT' and joint['version']=='1.0'
 parity=json.loads((R/'publication/editorial/BILINGUAL_PARITY.json').read_text(encoding='utf-8'));assert parity['status']=='PASS' and len(parity['pairs'])==4
 expected={'PAPER_I':('The exact block-type spectrum in the Colbourn–Dinitz–Rosa problem','El espectro exacto de tipos de bloque en el problema de Colbourn–Dinitz–Rosa','spectrum'),'PAPER_II':('A proof of the Colbourn–Dinitz–Rosa conjecture','Una demostración de la conjetura de Colbourn–Dinitz–Rosa','profiles')}
 count=0
 for paper,(en,es,stem) in expected.items():
  P=R/'preprints'/paper;V=P/'02_validation';report=json.loads((V/'AUDIT_RESULT.json').read_text(encoding='utf-8'));visual=json.loads((V/'VISUAL_REVIEW.json').read_text(encoding='utf-8'));assert report['status']=='PASS_LOCAL_DOCUMENT_CHECKS' and visual['status']=='PASS'
  entry=next(p for p in idx['papers'] if p['directory']=='preprints/'+paper)
  assert entry['title']==en and entry['title_es']==es
  main_pair=next(p for p in parity['pairs'] if p['paper']==paper and p['kind']==stem)
  assert main_pair['titles']=={'en':en,'es':es}
  for lang,title in [('en',en),('es',es)]:assert (P/f'01_manuscript/{stem}_{lang}.md').read_text(encoding='utf-8').splitlines()[0]=='# '+title
  for d in report['documents']:
   md=R/d['source'];pdf=md.with_suffix('.pdf');tex=md.with_suffix('.tex');b=json.loads((V/(md.stem+'_build.json')).read_text(encoding='utf-8'))
   assert sha(md)==d['markdown_sha256']==b['md'];assert sha(tex)==d['tex_sha256']==b['tex'];assert sha(pdf)==d['pdf_sha256']==b['pdf'];assert b['compile_passes']==2 and not b['layout_issues'];assert sha(P/b['log'])==b['log_sha256'];assert visual['pdfs'][pdf.relative_to(R).as_posix()]==sha(pdf)
   assert 'Preprint 1.0' in md.read_text(encoding='utf-8')
   assert d['printed_reference_urls']['status']=='PASS' and d['printed_reference_urls']['count']>0
   count+=1
  manifest=json.loads((P/'04_integrity/MANIFEST.json').read_text(encoding='utf-8'))
  for n,h in manifest.items():assert sha(P/n)==h,(paper,n)
 assert count==8
 for pair in parity['pairs']:assert len(set(pair['heading_counts'].values()))==1 and pair['formal_identifiers_equal']
 archive=R/'archives/CDR_shared_Lean_source_7643193.zip';assert sha(archive)==idx['shared_source_sha256']
 with zipfile.ZipFile(archive) as z:
  source=z.read('CDRBicolour/Absorption/Refined/Completion.lean').decode('utf-8-sig');assert 'theorem cdr_prescribed_intersection : PrescribedIntersection' in source
 axioms=(R/'publication/audit/recorded_axioms.txt').read_text(encoding='utf-8');assert "'CDRBicolour.Absorption.Refined.cdr_prescribed_intersection' depends on axioms: [propext, Classical.choice, Quot.sound]" in axioms
 for name in ['spectrum_en','spectrum_es']:
  text=(R/f'preprints/PAPER_I/01_manuscript/{name}.md').read_text(encoding='utf-8');assert 'Refined/Completion.lean' in text and ('complete formal proof' in text.lower() or 'prueba formal completa' in text.lower())
 for name in ['profiles_en','profiles_es']:
  text=(R/f'preprints/PAPER_II/01_manuscript/{name}.md').read_text(encoding='utf-8');assert 'a-6k-5' in text and 'n=y^2+2y+4\\le487' in text
  assert r'$3\mid n$' in text and r'$3\nmid n$' in text and '$m_2=3$' in text
 return dict(status='PASS',version='1.0',documents=count,bilingual_pairs=4,mathematical_sources_changed=False,fresh_lean_build=False,scope='Internal release, source, metadata, semantic and rendered-artifact checks; not peer review')
if __name__=='__main__':print(json.dumps(check(),indent=2))
