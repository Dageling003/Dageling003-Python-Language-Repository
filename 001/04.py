"""
4. BMI 计算器：输入身高(m)和体重(kg)，计算 BMI = 体重 / 身高²，保留 2 位小数输出。
"""
print("=======BMI 计算器：=============")
height = float(input("输入身高(m)："))   
weight = float(input("输入体重(kg):"))
bmi = weight / (height * height)
print(f"bmi={bmi:.2f}")
print("===============================")