"""
4. 定义一个全局变量，在函数内用 global 修改它，输出验证修改是否生效。
"""
# 定义全局变量
count = 10

def modify_global():
    # 声明要使用全局变量
    global count

    # 修改全局变量的值
    count = count + 5
    print(f"函数内部的 count 值为: {count}")

# 调用前打印
print(f"调用函数前的 count 值为: {count}")

# 调用函数
modify_global()

# 调用后再次打印，验证修改是否生效
print(f"调用函数后的 count 值为: {count}")
