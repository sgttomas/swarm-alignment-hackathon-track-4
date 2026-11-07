"""Read retained gzip JSON as data; inspect identity/delivery/reference boundaries."""
import gzip,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'sources'
rows=[]
for path in sorted(ROOT.glob('emergent-*-rep001.json.gz')):
 with gzip.open(path,'rb') as f: raw=f.read(200_000_001)
 if len(raw)>200_000_000: raise ValueError('expanded cap')
 d=json.loads(raw); run={'file':path.name,'expanded_bytes':len(raw),'expanded_sha256':hashlib.sha256(raw).hexdigest(),'run_id':d['run_id'],'condition_id':d['condition_id'],'sequence_id':d['sequence_id'],'episode_count':len(d['results']),'episodes':[]}
 for e in d['results']:
  events={x['event_id']:x for x in e['events']}; delivered=e['channel_transcript']
  delivery_matches=all(events[x['event_id']]['success'] is True and events[x['event_id']]['content']==x['content'] and events[x['event_id']]['actor']==x['sender'] for x in delivered)
  er={'episode_index':e['episode_index'],'task_type':e['task_type'],'task_ids':e['task_ids'],'group':e['group'],'verdict_policy':e['verdict_policy'],'reward_by_agent':e['reward_by_agent'],'channel_events_exact':delivery_matches,'message_count':len(delivered),'failed_sends':[{'event_id':x['event_id'],'actor':x['actor'],'error':x.get('error'),'chars':len(x.get('content',''))} for x in e['events'] if x['tool']=='send_message' and not x['success']],'agents':{}}
  for a,s in e['agents'].items():
   rawlog=json.dumps(s['private_raw_log'],ensure_ascii=False,separators=(',',':'))
   getlogs=[]
   actual_verdict_prompts=[]
   for mi,message in enumerate(s['messages']):
    content=message.get('content')
    if message.get('role')=='user' and isinstance(content,str) and f'## Episode {e["episode_index"]+1}: verdict phase' in content:actual_verdict_prompts.append({'message_index':mi,'content':content})
    if message.get('role')=='tool' and isinstance(content,str):
     try: payload=json.loads(content)
     except ValueError: continue
     if isinstance(payload,dict) and isinstance(payload.get('raw_log'),str):getlogs.append({'message_index':mi,'raw_log':payload['raw_log']})
   last_getlog=getlogs[-1] if getlogs else None
   sent=[x['content'] for x in delivered if x['sender']==a]
   er['agents'][a]={'task_id':s['task_id'],'last_getlog_matches_raw_log':bool(last_getlog and last_getlog['raw_log']==rawlog),'last_getlog_message_index':last_getlog['message_index'] if last_getlog else None,'actual_verdict_prompts':actual_verdict_prompts,'summary_verdict_prompt_matches_actual':any(x['content']==s['verdict_prompt'] for x in actual_verdict_prompts),'raw_log_chars':len(rawlog),'delivered_chars':sum(map(len,sent)),'maximum_message_chars':max(map(len,sent),default=0),'complete_rawlog_exact_substring_in_deliveries':rawlog in ''.join(sent),'verdict':s['verdict'],'verdict_correct':s['verdict_correct'],'verdict_forced':s['verdict_forced'],'task_expected_verdict':s['expected_verdict'],'verdict_submission':s['verdict_submission'],'evaluation_keys':[k for k in ['code_eval','extraction_eval','data_search_eval'] if s[k] is not None]}
  run['episodes'].append(er)
 rows.append(run)
(ROOT/'trace-inspection.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
for r in rows:
 print(r['file'],r['expanded_bytes'])
 for e in r['episodes']:
  print(e['episode_index'],e['task_type'],e['channel_events_exact'],'failed',len(e['failed_sends']),[(a,s['verdict'],s['task_expected_verdict'],s['raw_log_chars'],s['delivered_chars'],s['complete_rawlog_exact_substring_in_deliveries']) for a,s in e['agents'].items()])
