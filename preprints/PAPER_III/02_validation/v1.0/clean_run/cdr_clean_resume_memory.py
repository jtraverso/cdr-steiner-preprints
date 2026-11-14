from pathlib import Path
import subprocess,json,hashlib,datetime,os,threading,time,re,shutil
run=Path('C:/nw/cdr-clean-20261113'); root=run/'snapshot/lean'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((run/'status.json').read_text())
assert state['phase']=='FAILED'
state.pop('error',None);state.pop('build_exit_code',None);state['threads']=1
# The process inventory was checked immediately before launching this runner.
assert not (run/'build_attempt7.log').exists()
shutil.copyfile(run/'status.json',run/'status_attempt7.json')
shutil.copyfile(run/'build.log',run/'build_attempt7.log')
before=json.loads((run/'SOURCES_BEFORE.json').read_text())
assert all(sha(root/name)==value for name,value in before.items())
config_before=json.loads((run/'CONFIGS_BEFORE_FINAL.json').read_text())
assert all(sha(root/name)==value for name,value in config_before.items())
cache={str(p.relative_to(root)):sha(p) for p in (root/'.lake/build').rglob('*') if p.is_file()}
(run/'RESUME_CACHE_HASHES_7.json').write_text(json.dumps(cache,indent=2))
assert all(sha(root/name)==value for name,value in cache.items())
(run/'MEMORY_RESUME_7.json').write_text(json.dumps({'reason':'BRIUniform failed with std::bad_alloc; reduce LEAN_NUM_THREADS from4 to1 to reduce concurrent module memory pressure; no mathematical edits','launch_policy':'Detached hidden process; independent of unified exec session', 'resumed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'absence_of_surviving_build_processes_verified':True,'sources_validated':len(before),'configuration_hashes_validated':config_before,'same_run_artifacts_hashed_and_reread':len(cache),'project_modules_retained':len(list((root/'.lake/build/lib/lean').rglob('*.olean'))),'mathematical_sources_changed':False,'cache_policy':'Only objects produced in this clean reconstruction; Lake revalidates dependency traces'},indent=2))
state['pid']=os.getpid(); state['phase']='resuming'; state.pop('child_pid',None)
lock=threading.Lock()
def save():
    with lock:
        state['heartbeat']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        for attempt in range(100):
            try:
                tmp=run/'status.tmp';tmp.write_text(json.dumps(state,indent=2));tmp.replace(run/'status.json');return
            except PermissionError:time.sleep(.1)
        raise RuntimeError('Status file remained locked for ten seconds')
def beat():
    while True:save();time.sleep(10)
threading.Thread(target=beat,daemon=True).start()
def command(args,name):
    state['phase']=name;state['command']=args;save()
    with (run/(name+'.log')).open('w',encoding='utf-8') as log:
        proc=subprocess.Popen(args,cwd=root,stdout=log,stderr=subprocess.STDOUT,env={**os.environ,'LEAN_NUM_THREADS':'1'})
        state['child_pid']=proc.pid;save();code=proc.wait()
    state[name+'_exit_code']=code;save()
    if code:raise RuntimeError(f'{name} failed: {code}')
try:
    command(['lake','--no-cache','--fail-fast','build','CDRIII'],'build')
    command(['lake','env','lean','checks/Axioms.lean'],'axioms')
    config_after={name:sha(root/name) for name in config_before}
    (run/'CONFIGS_AFTER_FINAL.json').write_text(json.dumps(config_after,indent=2));assert config_before==config_after
    after={str(p.relative_to(root)).replace('\\','/'):sha(p) for p in root.rglob('*.lean') if '.lake' not in p.relative_to(root).parts}
    (run/'SOURCES_AFTER.json').write_text(json.dumps(after,indent=2));assert before==after
    found=re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]",(run/'axioms.log').read_text(),re.S)
    assert len(found)==4
    assert all(set(re.findall(r'[A-Za-z_][\w.]*',body))<={'propext','Classical.choice','Quot.sound'} for name,body in found)
    objects={str(p.relative_to(root)):sha(p) for p in (root/'.lake/build').rglob('*') if p.is_file()}
    (run/'OBJECT_HASHES.json').write_text(json.dumps(objects,indent=2))
    state['phase']='PASS';state['axiom_audits']=found;state['sources_unchanged']=True;save()
    (run/'report.json').write_text(json.dumps(state,indent=2))
except Exception as exc:
    state['phase']='FAILED';state['error']=repr(exc);save();(run/'report.json').write_text(json.dumps(state,indent=2));raise
