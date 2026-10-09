"""
综合题二：通用日志装饰器（任意参数 + 返回值）
需求：写一个装饰器 log，要求能装饰任意函数：
- 执行前打印：函数名、收到的位置参数和关键字参数
- 执行后打印：函数名、返回值
- 被装饰函数的返回值必须原样带出来，不能丢
自测：分别用一个无参无返回值函数和一个带多个参数、有返回值的函数装饰验证；如果带返回值的函数经过装饰后拿到的是 None。
"""
import functools
def log(func):
    """
        通用日志装饰器：打印函数名、参数和返回值
        """
    @functools.wraps(func)  # 保留原函数的元信息（如 __name__、__doc__）
    def wrapper(*args,**kwargs):
        # 执行前打印：函数名、位置参数、关键字参数
        print(f"[开始] 调用函数: {func.__name__}")
        print(f"  位置参数 args: {args}")
        print(f"  关键字参数 kwargs: {kwargs}")

        # 调用原始函数，并保存返回值
        result = func(*args, **kwargs)

        # 执行后打印：函数名、返回值
        print(f"[结束] 函数 {func.__name__} 返回: {result}")
        print("-" * 40)

        # 原样返回结果，保证不丢失
        return result
    return wrapper

@log
def say_hello():
    """无参无返回值函数"""
    print("你好！我是无参无返回值函数。")

@log
def add(a, b, c=0):
    """带多个参数、有返回值的函数"""
    print(f"计算 {a} + {b} + {c}")
    return a + b + c

if __name__ == "__main__":
    print("===== 测试1：无参无返回值 =====")
    ret1 = say_hello()
    print(f"say_hello() 的返回值是: {ret1}")

    print(f"===== 测试2：多参数有返回值 =====")
    ret2 = add(10, 20, c=30)
    print(f"add(10,20,c=30) 的返回值是: {ret2}")