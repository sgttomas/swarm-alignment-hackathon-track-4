"""Fetch exactly three preselected runs as inert JSON, no remote code execution."""
from pathlib import Path
import subprocess,datetime,hashlib,json
root=Path(__file__).resolve().parents[1];dst=root/'sources'/'narcbench';dst.mkdir(exist_ok=True)
rev='19cb14b269e052b19ba6d2bd2f4519afd3b10c57';base=f'https://huggingface.co/datasets/aaronrose227/narcbench/resolve/{rev}/scenarios/qwen3_32b/core/'
records=[]
for run in ['deception__audit_01__collusion','deception__audit_01__control','deception__audit_02__collusion']:
 for f in ['run_config.json','results.json','agent_prompts.json']:
  path=dst/(run+'--'+f);url=base+run+'/'+f;start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  proc=subprocess.run(['curl','-sS','-L','--max-time','30','--max-filesize','1048576','-o',str(path),'-w','%{http_code}',url],capture_output=True,text=True)
  b=path.read_bytes() if path.exists() else b''
  record={'source_url':url,'local_file':path.name,'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'curl_exit':proc.returncode,'http_status':proc.stdout,'stderr':proc.stderr,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()};records.append(record)
  if proc.returncode!=0 or proc.stdout!='200':raise RuntimeError(record)
  o=json.loads(b);print(run,f,len(b),list(o) if isinstance(o,dict) else type(o).__name__)
(dst/'acquisition.json').write_text(json.dumps(records,indent=2))
