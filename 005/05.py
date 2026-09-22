"""
5. 用列表存多个学生字典（含 name、score），遍历输出每人的等级，并计算全班平均分。
"""
# 定义学生列表，每个学生是一个字典
students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 82},
    {"name": "小刚", "score": 67},
    {"name": "小丽", "score": 73},
    {"name": "小华", "score": 58}
]

# 定义评分等级的规则
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

# 遍历学生列表，输出姓名、分数和等级
total_score = 0
for student in students:
    grade = get_grade(student["score"])
    total_score += student["score"]
    print(f"姓名: {student['name']}, 分数: {student['score']}, 等级: {grade}")

# 计算并输出平均分
average_score = total_score / len(students)
print(f"\n全班平均分: {average_score:.2f}")
