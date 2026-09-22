"""
1. 用 try/except 处理"打开不存在的文件"的错误：打不开就改为新建。
"""
# 尝试打开不存在的文件，失败则新建
filename = "test.txt"

try:
    with open(filename, 'r') as f:
        content = f.read()
        print(f"文件内容: {content}")
except FileNotFoundError:
    print(f"文件 {filename} 不存在，正在创建新文件...")
    with open(filename, 'w') as f:
        f.write("这是新创建的文件")
    print("文件创建成功！")