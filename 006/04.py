"""
4. 用 sorted(students, key=lambda s: s["score"]) 按分数升序排列学生列表并输出。
"""
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 95},
    {"name": "孙七", "score": 88}
]

sorted_students =sorted(students, key=lambda s: s["score"])

print("按分数升序排列的学生列表：")
for student in sorted_students:
    print(f"姓名：{student['name']}，分数：{student['score']}")