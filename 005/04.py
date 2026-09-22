"""
4. 字典 phone = {"张三":"110","李四":"120"}：取出某人的号码、新增一项、遍历打印所有键值。
"""
phone ={"张三":"110","李四":"120"}
# 1. 取出某人的号码（例如张三）
print(phone["张三"])

# 2. 新增一项（例如王五:119）
phone["王五"] = "119"
print(phone)

# 3. 遍历打印所有键值对
for name, number in phone.items():
    print(f"{name}: {number}")