"""Bounded public GET capture. URLs are operator-chosen publisher routes, never payload URLs."""
import datetime,hashlib,json,pathlib,sys,urllib.request,urllib.error,urllib.parse
ROOT=pathlib.Path(__file__).resolve().parents[1]/'sources'
def acquire(name,url,limit=5_000_000):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat(); rec={'file':name,'url':url,'start_utc':start}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Apart-formation-source-inspection/1.0'})
  with urllib.request.urlopen(req,timeout=35) as r:
   data=r.read(limit+1)
   if len(data)>limit:raise ValueError('capture exceeds cap')
   rec.update(status=r.status,final_url=urllib.parse.urlunsplit(urllib.parse.urlsplit(r.url)._replace(query="",fragment="")),headers={k:v for k,v in r.headers.items() if k.lower() in ['content-type','etag','last-modified','content-length']})
  (ROOT/name).write_bytes(data);rec.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e:rec.update(error=str(e))
 rec['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 p=ROOT/'acquisition.json'; rows=json.loads(p.read_text()) if p.exists() else [];rows.append(rec);p.write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rec))
if __name__=='__main__':acquire(sys.argv[1],sys.argv[2])
