"""
3. 给计算器加上异常处理：输入非数字或除数为 0 时给出友好提示，程序不崩溃。

"""
def calculator():
    while True:
        user_input = input("请输入表达式（如 5+3，输入q退出）：")
        if user_input.lower() == 'q':
            break

        try:
            # 简单解析：假设格式为 "数字 运算符 数字"
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("格式错误，请按 '数字 运算符 数字' 格式输入")

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("除数不能为0！")
                result = num1 / num2
            else:
                raise ValueError(f"不支持的运算符：{operator}")

            print(f"结果：{result}")

        except ValueError as ve:
            print(f"输入错误：{ve}")
        except ZeroDivisionError as ze:
            print(f"数学错误：{ze}")
        except Exception as e:
            print(f"未知错误：{e}")


calculator()