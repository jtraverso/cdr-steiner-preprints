from pathlib import Path
import json,hashlib,datetime,re,shutil
run=Path('C:/nw/cdr-clean-20261113');root=run/'snapshot/lean'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((run/'report.json').read_text(encoding='utf-8'))
assert state['build_exit_code']==state['axioms_exit_code']==0
assert 'UnicodeDecodeError' in state['error']
shutil.copyfile(run/'report.json',run/'report_postprocess_encoding_failure.json')
before=json.loads((run/'SOURCES_BEFORE.json').read_text(encoding='utf-8'))
config_before=json.loads((run/'CONFIGS_BEFORE_FINAL.json').read_text(encoding='utf-8'))
state.pop('error');state['postprocessing_fix']='Explicit UTF-8 log decoding; no Lean rebuild or source edits'
def save():
    state['heartbeat']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (run/'status.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
try:
    config_after={name:sha(root/name) for name in config_before}
    (run/'CONFIGS_AFTER_FINAL.json').write_text(json.dumps(config_after,indent=2));assert config_before==config_after
    after={str(p.relative_to(root)).replace('\\','/'):sha(p) for p in root.rglob('*.lean') if '.lake' not in p.relative_to(root).parts}
    (run/'SOURCES_AFTER.json').write_text(json.dumps(after,indent=2));assert before==after
    found=re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]",(run/'axioms.log').read_text(encoding='utf-8'),re.S)
    assert len(found)==4
    assert all(set(re.findall(r'[A-Za-z_][\w.]*',body))<={'propext','Classical.choice','Quot.sound'} for name,body in found)
    objects={str(p.relative_to(root)):sha(p) for p in (root/'.lake/build').rglob('*') if p.is_file()}
    (run/'OBJECT_HASHES.json').write_text(json.dumps(objects,indent=2))
    state['phase']='PASS';state['axiom_audits']=found;state['sources_unchanged']=True;save()
    (run/'report.json').write_text(json.dumps(state,indent=2))
except Exception as exc:
    state['phase']='FAILED';state['error']=repr(exc);save();(run/'report.json').write_text(json.dumps(state,indent=2));raise
