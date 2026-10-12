"""按给定正式PDF页码保存高清核对页，并记录当前成品校验和。"""
from pathlib import Path
import argparse
import hashlib
import json
import fitz

ROOT=Path(__file__).resolve().parents[1]
LABELS={'paper':'试卷','student':'学生详解','teacher':'教师备课'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('pages',nargs='+',help='例如 student:24 teacher:35')
    args=parser.parse_args();dest=ROOT/'preview/formal/hd';dest.mkdir(exist_ok=True)
    record={}
    for target in args.pages:
        kind,page=target.split(':');number=int(page);path=ROOT/'output'/f'第027套_{LABELS[kind]}版.pdf'
        doc=fitz.open(path);assert 1<=number<=len(doc)
        doc[number-1].get_pixmap(matrix=fitz.Matrix(1.65,1.65),alpha=False).save(dest/f'{kind}-{number:03}.png')
        if kind not in record:record[kind]=dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pages=[])
        record[kind]['pages'].append(number)
    (dest/'rendered-pages.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record,ensure_ascii=False))

if __name__=='__main__':main()



