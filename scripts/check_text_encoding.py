"""Reject invalid UTF-8 and common UTF-8/legacy-encoding corruption in active text."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
BAD=re.compile(r'\ufffd|\u00e2\u20ac|\u00e2[\u0080-\u00bf]|\u00c3[\u0080-\u00bf]|\u00c2[\u0080-\u00bf]')
EXT={'.md','.tex','.json','.cff','.bib','.py','.toml','.yml','.yaml','.txt'}
def suspicious(text):return BAD.search(text) is not None
def strings(value):
 if isinstance(value,str):yield value
 elif isinstance(value,list):
  for x in value:yield from strings(x)
 elif isinstance(value,dict):
  for k,v in value.items():yield str(k);yield from strings(v)
def check(root=ROOT):
 files=values=0;bad=[]
 for p in sorted(root.rglob('*')):
  if not p.is_file() or p.suffix.lower() not in EXT:continue
  rel=p.relative_to(root)
  if '.git' in rel.parts or '__pycache__' in rel.parts or 'compiler_logs' in rel.parts or rel.parts[0]=='archives' or rel.parts[:2]==('publication','audit'):continue
  try:text=p.read_bytes().decode('utf-8')
  except UnicodeDecodeError:bad.append(rel.as_posix()+': invalid UTF-8');continue
  files+=1
  if suspicious(text):bad.append(rel.as_posix()+': suspicious encoded text')
  if p.suffix=='.json':
   for value in strings(json.loads(text)):
    values+=1
    if suspicious(value):bad.append(rel.as_posix()+': suspicious JSON string');break
 if bad:raise ValueError('Encoding validation failed: '+'; '.join(bad))
 return dict(status='PASS',text_files=files,json_strings=values,scope='Active publication text; unchanged archives, archived audit transcripts and compiler logs excluded.')
if __name__=='__main__':print(json.dumps(check(),indent=2))
