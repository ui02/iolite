import re

INPUT_FILE = "output.md"
OUTPUT_FILE = "timeline.md"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

blocks = text.split("---")

result = []

for block in blocks:
    if "date:" not in block:
        continue

    # date
    date = re.search(r"\*\*date:\*\*\s*(.*)", block)
    date = date.group(1).strip() if date else ""

    # tags
    tags = re.findall(r"\*\*tags:\*\*\s*(.*)", block)
    tags = tags[0].split(",") if tags else []

    # image
    img = re.search(r"!\[\]\((.*?)\)", block)
    img = img.group(1) if img else ""

    # caption（画像後の文章）
    caption_match = re.split(r"!\[\]\(.*?\)", block)
    caption = caption_match[1].strip() if len(caption_match) > 1 else ""

    # timeline item生成
    item = f"""
{{{{< timelineItem icon="twitter" header="" badge="" subheader="{date}" >}}}}
  <img src="{img}">
  {caption}
"""

    for t in tags:
        t = t.strip()
        if t:
            item += f'  {{{{< badge >}}}}{t}{{{{< /badge >}}}}\n'

    item += "{{< /timelineItem >}}\n"

    result.append(item)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(result))

print("DONE → timeline.md")