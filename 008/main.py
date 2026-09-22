import my_math

print("=== 主程序调用 my_math 模块 ===")

# 调用模块函数
a, b = 10, 20
sum_result = my_math.add(a, b)
product_result = my_math.mul(a, b)

print(f"{a} + {b} = {sum_result}")
print(f"{a} × {b} = {product_result}")

# 更多示例
numbers = [(3, 7), (15, 25), (100, 200)]
for x, y in numbers:
    print(f"add({x}, {y}) = {my_math.add(x, y)}, mul({x}, {y}) = {my_math.mul(x, y)}")