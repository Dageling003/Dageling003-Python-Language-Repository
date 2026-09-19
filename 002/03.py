"""
3. 输入成绩(0~100)，输出等级：>=90 优秀，>=80 良好，>=60 及格，否则不及格。
"""
score =int(input(f"输入成绩(0~100):"))
if score >=90:
    print(f"优秀")
elif score >=80:
    print(f"良好")
elif score >=60:
    print(f"及格")
else:
    print(f"不及格")