"""
4. 把学生成绩按"姓名:分数"逐行写入文件，再读回文件计算并输出平均分。
"""
# 写入学生成绩
students = ["张三:85", "李四:92", "王五:78", "赵六:95"]
with open("scores.txt", "w", encoding="utf-8") as f:
    for student in students:
        f.write(student + "\n")

# 读取并计算平均分
total_score = 0
count = 0

with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            name, score = line.split(":")
            total_score += int(score)
            count += 1

if count > 0:
    average = total_score / count
    print(f"总人数：{count}，平均分：{average:.2f}")
else:
    print("没有数据")