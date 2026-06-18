import os
import re
from collections import Counter

TAG_PATTERN = re.compile(
    r"\{\{<\s*badge\s*>\}\}(.*?)\{\{<\s*/badge\s*>\}\}",
    re.DOTALL
)

counter = Counter()

TARGET_DIR = r"C:\Users\YURI\iolite\content\murmur2"

for root, dirs, files in os.walk(TARGET_DIR):

    for file in files:

        if not file.endswith(".md"):
            continue

        path = os.path.join(root, file)

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

        tags = TAG_PATTERN.findall(text)

        for tag in tags:

            tag = tag.strip()

            if tag:
                counter[tag] += 1

print("\n===== TAG RANKING =====\n")

for tag, count in counter.most_common():

    print(f"{count:4}  {tag}")

print("\n=======================\n")
print("種類数:", len(counter))
print("総タグ数:", sum(counter.values()))