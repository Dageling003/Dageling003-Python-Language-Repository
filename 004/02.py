"""
2. 定义 is_even(n) 返回 n 是否为偶数，并调用验证。
"""
def is_even(n):
    if n%2==0:
        return print(f"偶数")
    else:
        #多加需求 测试
        return print(f"不是偶数")

is_even(9)