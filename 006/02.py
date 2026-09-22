"""
2. 定义 my_sum(*args) 返回所有传入数字之和，并调用验证。
"""
def my_sum(*args):
    return sum(args)

result1 =my_sum(10,20)
print(f"my_sum(10, 20) = {result1}")

result2 = my_sum(1, 2, 3, 4, 5)
print(f"my_sum(1, 2, 3, 4, 5) = {result2}")

result3 = my_sum(100)
print(f"my_sum(100) = {result3}")

result4 = my_sum()
print(f"my_sum() = {result4}")

numbers_list = [7, 14, 21, 28]
# 注意这里的 * 号
result5 = my_sum(*numbers_list)
print(f"my_sum(*[7, 14, 21, 28]) = {result5}")

result6 = my_sum(1.5, 2, 3.7, 4)
print(f"my_sum(1.5, 2, 3.7, 4) = {result6}")