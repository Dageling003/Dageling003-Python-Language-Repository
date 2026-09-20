"""
3. 定义 add / sub / mul / div 四个函数及 calc(a, b, op)，主程序读入两数和运算符后调用 calc 输出结果。
"""
def add(a,b):
    """加法"""
    return a+b

def sub(a,b):
    """减法"""
    return a-b

def mul(a,b):
    """乘法"""
    return a*b

def div(a,b):
    """除法"""
    if b ==0:
        return "error"
    return a/b

def calc(a, b, op):
    if op == "+":
        return add(a,b)
    elif op == "-":
        return sub(a,b)
    elif op == "*":
        return mul(a,b)
    elif op =="/":
        return div(a,b)
    else:
        return "error"


# 主程序
if __name__ == "__main__":
    # 输入两个数和运算符
    a = float(input("请输入第一个数: "))
    b = float(input("请输入第二个数: "))
    op = input("请输入运算符(+、-、*、/): ")

    # 调用calc函数计算结果并输出
    result = calc(a, b, op)
    print(f"{a} {op} {b} = {result}")