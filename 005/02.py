"""
2. 字符串 s = "hello python"：输出 s[0]、s[-1]、反转 s[::-1]，并把其中的 Python 替换为 Java。
"""
s = "hello python"
# 1. 输出 s[0]
print(s[0])        # h

# 2. 输出 s[-1]
print(s[-1])       # n

# 3. 反转字符串
print(s[::-1])     # nohtyp olleh

# 4. 将 python 替换为 Java
new_s = s.replace("python", "Java")
print(new_s)       # hello Java