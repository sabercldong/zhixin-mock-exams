from pathlib import Path
import subprocess,hashlib,json,re
W=Path(__file__).parent
records=[]
for n in range(92,87,-1):
 p=W/f'verify_{n:03}.py';r=subprocess.run(['python3',str(p)],capture_output=True,text=True)
 assert r.returncode==0,(n,r.stdout,r.stderr)
 comments=re.findall(r'(?m)^    # Q(\d+): (.+)$',p.read_text());assert len(comments)==8
 records.append(dict(set=n,questions=[dict(question=int(q),check=name,passed=True) for q,name in comments],script_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),output=r.stdout.strip(),passed=True))
r=subprocess.run(['python3',str(W/'extra_checks.py')],capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr)
extra=json.loads((W/'extra_results.json').read_text());assert len(extra)==12 and all(x['passed'] for x in extra)
(W/'results.json').write_text(json.dumps(dict(papers=records,extra=extra),ensure_ascii=False,indent=2))
print('5套、40题关键结果及12项补充核验通过')
