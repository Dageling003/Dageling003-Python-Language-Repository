"""studentCMS.py —— 学生管理系统（Controller 层）

负责：在内存里用"一个列表"承载所有学员对象，提供增删改查接口，
并负责把数据持久化到文件（保存 / 加载）。
这是题目中第二个角色：学生管理系统。
"""


import os
import json
from student import Student


# 程序版本号（要求 1：显示版本信息），集中放在这里，供菜单使用
VERSION = "1.0.0"


class StudentCMS:
    """学生管理系统的核心控制器。

    维系统一的学生列表 self.students，所有增删改查都操作这一个列表；
    并负责 JSON 持久化。菜单与用户交互也收归到这里（run 方法），
    让 main.py 只做"创建实例 + 启动"这一件事。
    """

    def __init__(self, filename="students.json"):
        # 内存中用列表承载所有学员对象（动手前思考 1：列表 + 对象）
        self.students = []
        # 数据文件路径（目录可能还不存在，save 时再确保创建）
        # 延伸练习 5：文件名在创建系统对象时传入，一套代码可支撑多个班级
        self.file_path = os.path.join("data", filename)
        # 启动时尝试从文件加载历史数据（要求 5：再次启动能读回来）
        self.load()
        # 同步类属性"学员总数"
        Student.count = len(self.students)

    # ---------- 公共工具：读取合法整数 ----------

    @staticmethod
    def read_int(prompt="请输入年龄：", min_val=1, max_val=120, field_name="年龄"):
        """循环读取一个合法的整数（默认用于年龄校验，延伸练习 1）。

        把"读一个整数"收进类里做 @staticmethod（要求 7：不允许平铺独立函数），
        添加和修改时都能复用，输入非数字 / 越界都会提示重输，避免 int("abc") 直接崩溃。

        field_name 让提示语跟着业务字段走，而不是把"年龄"写死，
        以后读"分数""学号"等任意数值字段都能复用。
        """
        while True:
            s = input(prompt).strip()
            if not s.isdigit():           # 整数校验：必须由数字组成（挡掉负数/小数/字母/空串）
                print(f"{field_name}必须是整数，请重新输入。")
                continue
            val = int(s)
            if not (min_val <= val <= max_val):   # 范围校验
                print(f"{field_name}需在 {min_val}~{max_val} 之间，请重新输入。")
                continue
            return val

    # ---------- 公共查找（动手前思考 4：不要重复写三遍） ----------

    def find_student_by_name(self, name):
        """按姓名查找学员，是修改 / 删除 / 查询共用的枢纽方法。

        找到返回 Student 对象，未找到返回 None。
        （注：只返回第一个；若需支持同名多人，改这一处即可，符合"新增功能不改旧方法"。）
        """
        for stu in self.students:
            if stu.name == name:
                return stu
        return None

    # ---------- 1. 添加学员 ----------

    def add_student_interactive(self):
        """交互式录入一个新学员：逐项读取输入、校验后加入列表。"""
        name = input("请输入姓名：").strip()
        age = self.read_int("请输入年龄：", field_name="年龄")
        sex = input("请输入性别：").strip()
        phone = input("请输入联系方式：").strip()
        note = input("请输入描述信息：").strip()
        # 用统一的列表 self.students 承载，生成对象并加入
        self.students.append(Student(name, age, sex, phone, note))
        Student.count += 1
        print("添加成功！")

    # ---------- 2. 修改学员 ----------

    def update_student_interactive(self, name):
        """交互式修改：先按姓名找，找到则逐项更新，返回 True；找不到返回 False。"""
        stu = self.find_student_by_name(name)
        if not stu:
            return False
        # 找到后直接修改该对象的属性（年龄走整数校验）
        stu.age = self.read_int("请输入新年龄：", field_name="年龄")
        stu.sex = input("请输入新性别：").strip()
        stu.phone = input("请输入新联系方式：").strip()
        stu.note = input("请输入新描述信息：").strip()
        return True

    # ---------- 3. 删除学员 ----------

    def delete_student(self, name):
        """按姓名删除学员，成功返回 True，学员不存在返回 False。"""
        stu = self.find_student_by_name(name)
        if stu:
            self.students.remove(stu)
            Student.count -= 1
            return True
        return False

    # ---------- 4. 查询某个学员 ----------

    def show_student(self, name):
        """按姓名查询并打印单个学员信息；找不到给友好提示。"""
        stu = self.find_student_by_name(name)
        if stu:
            stu.show_info()
        else:
            print("该学员不存在。")

    # ---------- 5. 显示所有学员 ----------

    def show_all_students(self):
        """按行列出全部学员信息；没有数据时也给提示。"""
        if not self.students:
            print("当前还没有任何学员。")
            return
        print(f"\n共 {len(self.students)} 名学员：")
        for stu in self.students:
            print(f"{stu.name} | {stu.age} | {stu.sex} | "
                  f"{stu.phone} | {stu.note}")

    # ---------- 延伸练习 2：模糊查询（功能 7） ----------

    def search_by_keyword(self, keyword):
        """列出所有姓名或联系方式里包含关键词的学员。"""
        keyword = keyword.strip().lower()
        result = [s for s in self.students
                  if keyword in s.name.lower() or keyword in s.phone.lower()]
        if not result:
            print("没有匹配的学员。")
            return
        for stu in result:
            print(f"{stu.name} | {stu.age} | {stu.sex} | "
                  f"{stu.phone} | {stu.note}")

    # ---------- 6. 数据持久化 ----------

    def save(self):
        """将内存中的学员数据写入 JSON 文件。"""
        # 确保 data/ 目录存在，不存在则创建（实现提示：先确保目录有效再写入）
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as f:
            # 每个对象先转成字典，再整体写成 JSON
            json.dump(
                [s.to_dict() for s in self.students],
                f,
                ensure_ascii=False,  # 中文原样保存，不转成 \uXXXX
                indent=2,            # 缩进 2 空格，文件更易读
            )
        print(f"已保存 {len(self.students)} 条学员信息。")

    def load(self):
        """从 JSON 文件读取历史数据到内存（动手前思考 3：文件不存在/为空也不能崩）。"""
        # 文件不存在 → 直接返回，不报错（首次运行场景）
        if not os.path.exists(self.file_path):
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, ValueError):
            # 文件为空或 JSON 损坏 → 兜底为空列表，不崩
            self.students = []
            return
        # 文件内容不是列表（异常格式）→ 兜底为空
        if not isinstance(data, list):
            data = []
        # 逐条用 from_dict 重建 Student 对象（不用 eval，安全）
        self.students = [Student.from_dict(d) for d in data]

    # ---------- 菜单 + 主循环 ----------

    @staticmethod
    def show_menu():
        """打印主菜单（含版本号与学员总数，对应要求 1）。"""
        print(f"\n====== 学生管理系统 v{VERSION} ======")
        print(f"当前学员总数：{Student.count}")
        print("1. 添加学员")
        print("2. 修改学员")
        print("3. 删除学员")
        print("4. 查询学员")
        print("5. 显示所有学员")
        print("6. 保存信息")
        print("7. 模糊查询（按姓名/联系方式关键词）")
        print("0. 退出系统")
        print("======================================")

    def run(self):
        """启动系统主循环：显示菜单 → 读取选择 → 分派处理，直到用户确认退出。

        要求 6：可反复增删改查；只有用户确认退出时才结束。
        """
        while True:
            self.show_menu()
            # strip() 去掉首尾空白，避免误输入空格导致匹配失败
            choice = input("请输入功能序号：").strip()

            if choice == "1":
                self.add_student_interactive()

            elif choice == "2":
                name = input("请输入要修改的学员姓名：").strip()
                if self.update_student_interactive(name):
                    print("修改成功！")
                else:
                    print("该学员不存在。")

            elif choice == "3":
                name = input("请输入要删除的学员姓名：").strip()
                if self.delete_student(name):
                    print("删除成功！")
                else:
                    print("该学员不存在。")

            elif choice == "4":
                name = input("请输入要查询的学员姓名：").strip()
                self.show_student(name)

            elif choice == "5":
                self.show_all_students()

            elif choice == "6":
                self.save()

            elif choice == "7":
                keyword = input("请输入关键词：").strip()
                self.search_by_keyword(keyword)

            elif choice == "0":
                # 退出确认：兼容大写 Y 和小写 y（实现提示）
                ans = input("确定要退出吗？(Y/N)：").strip().lower()
                if ans == "y":
                    self.save()          # 退出前自动保存，避免忘记保存丢数据
                    print("再见！")
                    break
                # 其它任何输入都回到菜单继续

            else:
                # 输入字母、不存在的序号等非法输入：不崩、不退出，提示后重画菜单
                print("输入无效，请重新输入。")
