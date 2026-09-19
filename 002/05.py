"""
5. 简易计算器：输入两个数与运算符（+ - * /），输出结果；除数为 0 时输出"除数不能为0"。
"""
number_a = int(input("输入第1个数: "))
number_b = int(input("输入第2个数: "))
symbol_a = input("输入一个运算符(+ - * /): ")

if symbol_a == "+":
    result = number_a + number_b
elif symbol_a == "-":
    result = number_a - number_b
elif symbol_a == "*":
    result = number_a * number_b
elif symbol_a == "/":
    if number_b == 0:
        print("除数不能为0")
    else:
        result = number_a / number_b
else:
    print("无效的运算符")

# 只有在有计算结果时才打印
if symbol_a in ["+", "-", "*"] or (symbol_a == "/" and number_b != 0):
    print(f"{number_a} {symbol_a} {number_b} = {result}")