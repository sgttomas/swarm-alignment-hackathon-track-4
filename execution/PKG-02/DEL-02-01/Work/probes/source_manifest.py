"""Bind acquired sources to byte identity and observed acquisition end times."""
from pathlib import Path
import datetime,hashlib,json
root=Path(__file__).resolve().parents[1];p=root/'sources'
urls={
'swarmtraces.html':'https://swarmtraces.org/',
'swarm-redacted.jsonl.gz':'https://swarmtraces.org/data/final/redacted.jsonl.gz',
'swarm-viewer.html':'https://swarmtraces.org/viewer/',
'swarm-viewer.js':'https://swarmtraces.org/viewer/viewer.js',
'swarm-row-R0053434.json':'https://swarmtraces.org/api/row/R0053434',
'transluce.html':'https://transluce.org/agent-activity',
'transluce-data.zip':'https://transluce.org/data/urlquery-agent-activity-2026-09-23.zip',
'ai-village-metadata.json':'https://huggingface.co/api/datasets/aidigestorg/ai-village',
'urlquery-representative.html':'https://urlquery.net/report/81699969-91c3-4454-913e-1a015b3fde47',
'urlquery-terms.html':'https://urlquery.net/terms-and-conditions',
'narcbench/dataset-README.md':'https://huggingface.co/datasets/aaronrose227/narcbench/resolve/19cb14b269e052b19ba6d2bd2f4519afd3b10c57/README.md',
'narcbench/metadata_gen.json':'https://huggingface.co/datasets/aaronrose227/narcbench/resolve/19cb14b269e052b19ba6d2bd2f4519afd3b10c57/activations/qwen3_32b/core/metadata_gen.json',
}
records=[]
for name,url in urls.items():
 f=p/name;b=f.read_bytes();records.append({'local_file':name,'url':url,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'acquisition_end_utc_from_file_mtime':datetime.datetime.fromtimestamp(f.stat().st_mtime,datetime.timezone.utc).isoformat(),'method':'curl -L with timeout and size guard; static file capture; no payload execution'})
for r in json.loads((p/'narcbench/acquisition.json').read_text()):records.append(dict(r,local_file='narcbench/'+r['local_file']))
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':records,'limits':['Hashes identify retained bytes, not authenticity or completeness.','Source HTML text/link views omit script/style data through Python HTMLParser; no JavaScript ran.','URLQuery header copy omits Set-Cookie; captured response body remains unchanged.','Transluce extracted members retain archive bytes; package manifest checked separately.','Sources retained locally for research/review; raw redistribution not authorized by this acquisition.']}
(p/'ACQUISITION_MANIFEST.json').write_text(json.dumps(out,indent=2))
print('Bound',len(records),'sources')
