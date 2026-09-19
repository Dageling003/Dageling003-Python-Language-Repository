"""
4. 输入年份，判断并输出是否为闰年。
year /400 ==0
year /4==0 && year/100！=0
"""
year = int(input(f"请输入年份："))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")
