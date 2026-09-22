"""
1. 用 with open 把若干行文本写入 note.txt。
"""
lines = ["第一行内容", "第二行内容", "第三行内容"]
with open("note.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
