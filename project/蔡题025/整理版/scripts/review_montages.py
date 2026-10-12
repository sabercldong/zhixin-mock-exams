"""将已渲染的高清核对页按每图四页排成复审图；不修改正式成品。"""
from pathlib import Path
import json
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]

def main():
    directory = ROOT / 'preview/formal/hd'
    record = json.loads((directory / 'rendered-pages.json').read_text())
    index = []
    for kind, entry in record.items():
        pages = entry['pages']
        for start in range(0, len(pages), 4):
            group = pages[start:start + 4]
            canvas = Image.new('RGB', (2010, 2890), '#eeeeee')
            draw = ImageDraw.Draw(canvas)
            for position, number in enumerate(group):
                im = Image.open(directory / f'{kind}-{number:03}.png').convert('RGB')
                im.thumbnail((980, 1390), Image.Resampling.LANCZOS)
                x = 15 + (position % 2) * 1000
                y = 35 + (position // 2) * 1440
                draw.text((x, y - 22), f'{kind} PDF page {number}', fill='black')
                canvas.paste(im, (x, y))
            name = f'{kind}-hd-overview-{start // 4 + 1:02}.jpg'
            canvas.save(directory / name, quality=95)
            index.append(dict(file=name, kind=kind, pages=group, sha256=entry['sha256']))
    (directory / 'montage-index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')
    print(f'生成 {len(index)} 张高清复审图。')

if __name__ == '__main__':
    main()
