"""
4. 用循环打印右对齐直角三角形（共 5 行，第 i 行 i 个 *）。
"""
i =1
j =1
for i in range(1,6):
    for j in range(1,i+1):
        print(f"*",end="\t")
    print()
