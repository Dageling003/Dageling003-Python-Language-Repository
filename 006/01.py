"""
1. 定义函数一次返回最大值、最小值、平均值三个结果，在外部用三个变量接收并打印。
"""
def calculate_stats(numbers):
    """
    计算列表中数字的最大值、最小值和平均值。

    Args:
        numbers: 一个包含数字的列表。

    Returns:
        一个包含 (最大值, 最小值, 平均值) 的元组。
    """
    # 2. 计算各项统计量
    max_value = max(numbers)
    min_value = min(numbers)
    # 计算平均值：先求和，再除以个数
    average_value = sum(numbers) / len(numbers)

    # 3. 返回一个元组（注意：括号可以省略）
    return max_value, min_value, average_value

data_list =[11,99,54,100,28,70,33]

result_max, result_min, result_avg = calculate_stats(data_list)

print(f"数据列表: {data_list}")
print(f"最大值: {result_max}")
print(f"最小值: {result_min}")
print(f"平均值: {result_avg:.2f}")