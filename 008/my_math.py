"""
自定义数学模块
"""


def add(a, b):
    """加法函数"""
    return a + b


def mul(a, b):
    """乘法函数"""
    return a * b


if __name__ == "__main__":
    # 测试代码
    print("=== 模块自测 ===")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"mul(4, 6) = {mul(4, 6)}")

    # 更多测试
    test_cases = [(1, 2), (0, 100), (-5, 8), (2.5, 3.5)]
    for x, y in test_cases:
        print(f"add({x}, {y}) = {add(x, y)}, mul({x}, {y}) = {mul(x, y)}")