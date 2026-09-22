"""
3. 读取一个文本文件，统计每个单词（或字符）出现的次数并输出。
"""
from collections import Counter

with open("note.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 按单词统计（英文文本）
words = text.split()
word_count = Counter(words)

# 按字符统计（中文文本）
char_count = Counter(text.replace("\n", "").replace(" ", ""))

print("单词统计：", dict(word_count))
print("字符统计：", dict(char_count))