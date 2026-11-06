"""Rebuild document-level audit records and page renders from the delivered PDFs."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,sys
from check_reference_links import check as check_reference_links
import pymupdf as fitz
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]
Q=R.parent/'cdr_preprint_1_0_visual_QA'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,z):p.write_bytes((json.dumps(z,ensure_ascii=False,indent=2)+'\n').encode())
def norm_math(s):return re.sub(r'\s+','',re.sub(r'\\text\{[^}]*\}','TEXT',s)).strip('.,;')
def run():
 Q.mkdir(exist_ok=True);all_records=[];parity=[];titles=[];baseline=json.loads((R/'publication/editorial/PROTECTED_BASELINE.json').read_text(encoding='utf-8'))['documents']
 for paper,stem in [('PAPER_I','spectrum'),('PAPER_II','profiles')]:
  P=R/'preprints'/paper;V=P/'02_validation';records=[]
  for kind,folder in [(stem,'01_manuscript'),('companion','05_formalization')]:
   langs={l:(P/folder/f'{kind}_{l}.md').read_text(encoding='utf-8') for l in ['en','es']}
   math={l:[norm_math(t) for t in re.findall(r'\$\$(.*?)\$\$',s,re.S)] for l,s in langs.items()};assert math['en']==math['es'],(paper,kind,'display mismatch')
   ids={l:Counter(re.findall(r'CDRBicolour[./][A-Za-z0-9_./]+|Refined/[A-Za-z0-9_./]+\.lean',s)) for l,s in langs.items()};assert ids['en']==ids['es'],(paper,kind,'formal ID mismatch')
   parity.append(dict(paper=paper,kind=kind,displays=len(math['en']),formal_identifiers_equal=True,heading_counts={l:len(re.findall(r'^#{1,6} ',s,re.M)) for l,s in langs.items()},titles={l:s.splitlines()[0][2:] for l,s in langs.items()}))
   for lang,s in langs.items():
    md=P/folder/f'{kind}_{lang}.md';pdf=md.with_suffix('.pdf');tex=md.with_suffix('.tex');b=json.loads((V/f'{kind}_{lang}_build.json').read_text(encoding='utf-8'))
    for ext,path in [('md',md),('tex',tex),('pdf',pdf)]:assert sha(path)==b[ext],path
    assert b['compile_passes']==2 and not b['layout_issues'] and sha(P/b['log'])==b['log_sha256']
    assert 'Preprint 1.0' in s and not re.search(r'Review version 0\.7|Versi\u00f3n de revisi\u00f3n 0\.7|review-v0\.7',s)
    old=baseline[md.relative_to(R).as_posix()]
    if kind!='companion':
     pat=r'\*\*(?:Theorem|Teorema) 1(?:[ .(]).*?(?=\n\n)';assert old['main_statement']==re.search(pat,s,re.S).group(),(md,'main statement changed')
     oldmath=Counter(old['normalized_displays']);newmath=Counter(math[lang]);assert not (oldmath-newmath),(md,'protected display removed')
    renders=Q/paper/f'{kind}_{lang}';renders.mkdir(parents=True,exist_ok=True);doc=fitz.open(pdf);pages=[];thumbs=[];bounds=[]
    for i,page in enumerate(doc):
     pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False);png=renders/f'{i+1:02}.png';pix.save(png);im=Image.open(png).convert('RGB');im.thumbnail((320,465));tile=Image.new('RGB',(344,500),'#e5e7eb');tile.paste(im,((344-im.width)//2,23));ImageDraw.Draw(tile).text((12,480),f'{kind}_{lang} / {i+1}',fill='black');thumbs.append(tile)
     for block in page.get_text('dict')['blocks']:
      for line in block.get('lines',[]):
       for span in line['spans']:
        x0,y0,x1,y1=span['bbox']
        if x0 < -1 or y0 < -1 or x1>page.rect.width+1 or y1>page.rect.height+1:bounds.append(dict(page=i+1,bbox=span['bbox'],text=span['text']))
     pages.append(dict(page=i+1,sha256=sha(png),width=pix.width,height=pix.height))
    assert not bounds,(pdf,bounds)
    url_report=check_reference_links(md)
    cols=4;rows=(len(thumbs)+cols-1)//cols;sheet=Image.new('RGB',(cols*344,rows*500),'white')
    for i,tile in enumerate(thumbs):sheet.paste(tile,((i%cols)*344,(i//cols)*500))
    contacts=V/'renders';contacts.mkdir(exist_ok=True);contact=contacts/f'{kind}_{lang}.jpg';sheet.save(contact,quality=92)
    rec=dict(source=md.relative_to(R).as_posix(),markdown_sha256=sha(md),tex_sha256=sha(tex),pdf_sha256=sha(pdf),pages=len(doc),display_count=len(math[lang]),render_sha256=sha(contact),page_renders=pages,layout_issues=b['layout_issues'],compile_passes=2,printed_reference_urls=url_report)
    records.append(rec);all_records.append(rec)
  for pair in parity:
   if pair['paper']==paper:assert len(set(pair['heading_counts'].values()))==1
  save(V/'AUDIT_RESULT.json',dict(status='PASS_DOCUMENT_STATIC_CHECKS_VISUAL_REVIEW_PENDING',edition='1.0',documents=records,shared_math_revision='7643193',scope='Current artifact, bilingual and protected-display audit; archived Lean build reviewed, no fresh Lean compilation.',printed_proof_map='PRINTED_PROOFS.md'))
  save(V/'RENDER_INDEX.json',dict(version='1.0',renderer='PyMuPDF',scale=1.5,documents=[dict(source=z['source'],pdf_sha256=z['pdf_sha256'],contact_sha256=z['render_sha256'],page_renders=z['page_renders']) for z in records]))
  save(V/'SEMANTIC_CHANGE_REPORT.json',dict(edition='1.0',baseline='31db6b0',main_theorem_statements='UNCHANGED',protected_display_formula_multisets='BASELINE_PRESERVED_WITH_DOCUMENTED_ADDITIONS',authorized_changes=['Explicit equivalent composite-descent formulation with the square exception','Two overfull-subset calculations added; endpoint uses a-6k-5 under delta>=a-3','Mass-error estimate expanded','Theorem 6.2 proof status explicitly formal, incomplete written sketch replaced by a formal dependency guide','k<4 implies n<=487','Bilingual titles and preprint metadata aligned','Factor 3 explicitly takes priority as the outer factor','Printed full reference URLs','Symbolic proof status, elementary residual-intersection criterion and reproduction evidence for Theorem 6.2'],lean_sources_changed=False,unresolved_queries=[]))
 save(R/'publication/editorial/BILINGUAL_PARITY.json',dict(status='PASS',version='1.0',pairs=parity))
 save(R/'publication/editorial/ARTIFACT_AUDIT.json',dict(status='PASS_STATIC_VISUAL_REVIEW_PENDING',version='1.0',documents=all_records,full_page_render_count=sum(z['pages'] for z in all_records)))
 print(json.dumps(dict(status='PASS_STATIC_VISUAL_REVIEW_PENDING',documents=len(all_records),pages=sum(z['pages'] for z in all_records),qa_directory=str(Q)),indent=2))
if __name__=='__main__':run()
