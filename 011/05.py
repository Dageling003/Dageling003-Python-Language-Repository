"""
综合题五：统计调用次数（用闭包在装饰器里保存状态）
需求：写装饰器 count_calls，统计原函数被调用的次数：
- 内部用一个变量记录次数，每次调用打印「第 n 次调用」
- 不许用全局变量
动手前想清楚两件事：这个计数变量应该定义在哪一层？要不要 nonlocal？
附加思考：如果不用 int + nonlocal，而是用一个列表存次数（每次 append），
不用声明也能改——这两种写法行为上有什么区别？为什么列表可以不声明？（这道想明白，闭包的作用域就真懂了）
"""
def count_calls(func):
    count = 0  # 计数变量定义在装饰器外层，被 wrapper 引用形成闭包，全程不使用全局变量
    def wrapper(*args, **kwargs):
        nonlocal count  # 声明 count 是外层作用域的变量，这样对它重新赋值才不会新建局部变量
        count += 1      # 每次调用都让外层闭包里的 count 自增 1
        print(f"第 {count} 次调用")
        return func(*args, **kwargs)  # 调用原函数并原样返回其结果
    return wrapper  # 返回包装后的函数

@count_calls  # 等价于 say_hello = count_calls(say_hello)
def say_hello(name):
    print(f"Hello, {name}!")

# 三次调用共享同一个闭包里的 count，因此输出 第 1 / 2 / 3 次调用
say_hello("Alice")
say_hello("Bob")
say_hello("Tom")