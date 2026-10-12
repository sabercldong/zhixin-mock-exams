import re

def keep_math_leads(tex):
    """短引导句与紧随其后的公式同页，不改变字体、行距或段距。"""
    blocks = tex.split("\n\n")
    for i in range(len(blocks) - 1):
        lead = blocks[i].strip()
        if (blocks[i + 1].lstrip().startswith(r"\[")
                and re.search(r"[\u4e00-\u9fff]", lead)
                and not lead.startswith("\\")
                and len(lead.replace("\n", "")) <= 100):
            blocks[i] = blocks[i].rstrip() + r"\nopagebreak[4]"
    return "\n\n".join(blocks)

def pandoc_source(text):
 return text
