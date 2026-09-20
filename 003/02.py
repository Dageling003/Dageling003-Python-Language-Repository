"""
2. 用 for 打印九九乘法表。
"""
i =1
j =1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end="\t")
    print()
