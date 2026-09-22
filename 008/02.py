"""
2. 除零异常：用 try/except Exception as e 捕获并打印错误信息，finally 中打印"结束"。
"""
try:
    result = 10 / 0
except Exception as e:
    print(f"发生错误：{e}")
finally:
    print("结束")