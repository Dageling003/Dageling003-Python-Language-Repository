"""
3. 猜数字：随机生成 1~100 的整数，循环输入直到猜对，提示"大了/小了"，并输出猜测次数。
"""
import random
target = random.randint(1,100)
count = 0
while True:
    try:
        guess = int(input("请输入你猜的数字（1~100）："))
        count += 1

        if guess < target:
            print("小了")
        elif guess > target:
            print("大了")
        else:
            print(f"恭喜你猜对了！一共猜了{count}次。")
            break
    except ValueError:
        print("请输入有效的整数！")
