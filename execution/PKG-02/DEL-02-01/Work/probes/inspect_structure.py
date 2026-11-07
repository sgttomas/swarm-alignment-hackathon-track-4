"""Non-executing structure/sample qualification; no network, eval, or payload execution."""
from pathlib import Path
import collections,csv,datetime,gzip,hashlib,io,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'sources'
counts=collections.Counter(); keys=collections.Counter(); nbytes=0;samples={}; malformed=[]
with gzip.open(p/'swarm-redacted.jsonl.gz','rb') as f:
 for i,l in enumerate(f,1):
  nbytes+=len(l)
  if nbytes>200*1024**2:raise ValueError('Expanded inspection bound exceeded')
  try:o=json.loads(l)
  except (UnicodeDecodeError,json.JSONDecodeError) as e:
   malformed.append({'line':i,'error':type(e).__name__});continue
  keys.update(o.keys());counts['rows']+=1;counts['kind:'+o['kind']]+=1;counts['parent_nonnull']+=o.get('parent_id') is not None;counts['time_nonnull']+=o.get('time_utc') is not None
  tests={'first':i==1,'parented':o.get('parent_id') is not None,'timed':o.get('time_utc') is not None,'board_done':'zzHFPOSTRCE_US58_RECON_DONE' in o.get('text',''),'response_kind':'response' in o['kind']}
  for label,select in tests.items():
   if select and label not in samples:samples[label]={'line':i,'record':o}
# Resolve reconstruction parent from actually present ID, rather than infer actors.
parents={x['record']['parent_id'] for x in samples.values() if x['record'].get('parent_id')}
with gzip.open(p/'swarm-redacted.jsonl.gz','rt') as f:
 for i,l in enumerate(f,1):
  o=json.loads(l)
  if o['id'] in parents:samples['parent:'+o['id']]={'line':i,'record':o}
summary={'inspection_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':dict(counts),'expanded_bytes':nbytes,'keys':dict(keys),'malformed':malformed,'sample_selection':'first row, first nonnull parent, first nonnull time, first exact board marker named in source report, first response kind, and their reconstruction parents','sample_rows':samples}
(p/'swarm-structure-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print('swarm',dict(counts),'expanded',nbytes,'sample IDs',{k:v['record']['id'] for k,v in samples.items()})
with zipfile.ZipFile(p/'transluce-data.zip') as z:
 prefix='urlquery-agent-activity-2026-09-22-v5/'
 if sum(x.file_size for x in z.infolist())>200*1024**2:raise ValueError('ZIP expanded bound exceeded')
 manifest=json.loads(z.read(prefix+'manifest.json')); checks=[]
 # Retain full manifest independently; validation performed after examining its schema.
 rows=list(csv.DictReader(io.TextIOWrapper(z.open(prefix+'all-reports.csv'))))
 tc={k:dict(collections.Counter(r[k] for r in rows)) for k in ['disposition','confidence','timestamp_precision','broad_class']}
 duplicate_ids=len(rows)-len({r['report_id'] for r in rows})
 sample_ids={'d6669745-83d2-4628-82fa-87420ae6a5d7','4c62b534-a8e2-44d1-bddf-db92d4bf20a6','81699969-91c3-4454-913e-1a015b3fde47','4e2b6c8c-1f42-4d67-b2f2-c5da7877ffed'}
 selected=[dict(csv_data_row=i+1,**r) for i,r in enumerate(rows) if r['report_id'] in sample_ids]
 for disposition in ['background','review_required']:
  selected.append(next(dict(csv_data_row=i+1,**r) for i,r in enumerate(rows) if r['disposition']==disposition))
 out={'inspection_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fields':list(rows[0]),'row_count':len(rows),'duplicate_ids':duplicate_ids,'counts':tc,'sample_selection':'named March 6 failure/success sequence and reviewed confidence overrides from primary report/README, plus first background and review_required row','samples':selected,'archive_members':[dict(name=x.filename,expanded_bytes=x.file_size,compressed_bytes=x.compress_size) for x in z.infolist()]}
 (p/'transluce-structure-summary.json').write_text(json.dumps(out,indent=2));print('transluce',len(rows),duplicate_ids,tc)
