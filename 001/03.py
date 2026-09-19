"""
3. 用 f-string 输出一张名片：姓名、年龄、月薪（保留 2 位小数）。
"""
name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))
month_money = float(input("请输入你的月薪："))
print(f"我的名片：\n姓名:{name}、年龄:{age}、月薪:{month_money:.2f}")
