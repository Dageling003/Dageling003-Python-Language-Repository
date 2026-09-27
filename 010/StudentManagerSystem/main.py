"""main.py —— 程序入口（启动模块）

仅负责创建系统实例并启动主循环，
所有菜单交互与业务逻辑都交给 studentCMS.StudentCMS.run() 处理。
（验收标准 1：main.py 里只有启动逻辑。）
"""

from studentCMS import StudentCMS

# 这是 Python 的"程序入口守卫"：
# 只有当本文件被直接运行时（python main.py），下面的代码才会执行；
# 如果别的模块 import 了 main，这段不会触发，避免重复启动。
if __name__ == "__main__":
    # 创建系统实例（__init__ 内部会自动 load 历史数据），然后启动主循环。
    # 入口只做这两件事，职责单一、清晰。
    # 延伸练习 5：可传入 filename="class2.json" 支撑多个班级。
    StudentCMS().run()
