"""
2. 用 a 模式向该文件追加两行，再读取验证原有内容没有丢失
"""
# 追加两行
with open("note.txt", "a", encoding="utf-8") as f:
    f.write("第四行内容\n")
    f.write("第五行内容\n")

# 读取验证原有内容没有丢失
with open("note.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)