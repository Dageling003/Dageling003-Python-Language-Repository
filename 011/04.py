"""
综合题四：双装饰器与执行顺序
需求：写两个装饰器 a 和 b，各自在原函数执行前后打印自己的进入/退出提示，再把它们同时装饰在同一个函数上。
- 先在纸上写出预期的完整输出，再运行验证
- 如果和预期不符，回正文第四节看「装饰由内到外，执行由外到内」
- 附加：把两个 @ 的顺序交换，先预测再验证
自测：两次运行共四份输出，你都要能解释「为什么是这个顺序」。
"""
def a(func):
    # func 是被装饰后的函数对象（这里即 b 返回的 wrapper_b）
    def wrapper(*args, **kwargs):
        print("enter a")            # 进入 a 装饰器：在原函数前打印
        result = func(*args, **kwargs)  # 调用下一层的函数（b 的 wrapper）
        print("exit a")             # 退出 a 装饰器：在原函数后打印
        return result              # 原样返回结果，不丢失返回值
    return wrapper

def b(func):
    # func 是最原始的函数 greet（还没被装饰时的版本）
    def wrapper(*args, **kwargs):
        print("enter b")            # 进入 b 装饰器：在最内层、离原函数最近
        result = func(*args, **kwargs)  # 调用原始函数 greet
        print("exit b")             # 退出 b 装饰器
        return result
    return wrapper

# 情况一：@a 在上，@b 在下
# 装饰由内到外：先 b(greet) -> wrapper_b，再 a(wrapper_b) -> wrapper_a
# 执行由外到内：调用 greet() 实际是 wrapper_a()，所以输出顺序为
#   enter a -> enter b -> hello -> exit b -> exit a
@a
@b
def greet():
    print(f"hello")
greet()

# 情况二：@b 在上，@a 在下
# 装饰由内到外：先 a(greet) -> wrapper_a，再 b(wrapper_a) -> wrapper_b
# 执行由外到内：调用 greet() 实际是 wrapper_b()，所以输出顺序为
#   enter b -> enter a -> hello -> exit a -> exit b
@b
@a
def greet():
    print(f"hello")
greet()