"""student.py —— 学员模型（Model 层）

只负责描述"一个学员"长什么样、能做什么，
不关心数据从哪来、存到哪、怎么展示。
这是题目中第一个角色：学员。把它独立成一个类，
以后要扩展（加班级、加成绩、加学号）时，只动这一个文件即可。
"""


class Student:
    """学员类：封装单个学生的信息。"""

    # 类属性：记录系统里当前一共有多少学员（延伸练习 3）。
    # 用类属性而不是实例属性，因为它的含义是"全体学员的总数"，与单个学员无关。
    count = 0

    def __init__(self, name, age, sex, phone, note):
        # 题目规定的 5 个属性：姓名、年龄、性别、联系方式、描述信息
        self.name = name
        self.sex = sex
        self.phone = phone          # 联系方式
        self.note = note            # 描述信息
        # 数值字段在"入口处"统一转成 int，保证内存里类型一致，后面运算不踩坑
        self.age = int(age)

    def show_info(self):
        """在控制台格式化打印该学员的完整信息。"""
        print("====== 学员信息 ======")
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"性别：{self.sex}")
        print(f"联系方式：{self.phone}")
        print(f"描述信息：{self.note}")
        print("======================")

    def to_dict(self):
        """把学员对象转换成字典，方便写入 JSON 文件。

        为什么需要它？因为 json 模块只认识 dict/list/str/int 这些基础类型，
        不认识我们自定义的 Student 对象，所以保存前必须先"拍平"成字典。
        """
        return {
            "name": self.name,
            "age": self.age,
            "sex": self.sex,
            "phone": self.phone,
            "note": self.note,
        }

    @classmethod
    def from_dict(cls, d):
        """由字典重建一个 Student 对象（加载文件时用）。

        用 @classmethod：拿到的是 cls（类本身）而不是 self，
        即使将来 Student 改名或派生子类，cls(...) 也能正确实例化，不用硬编码类名。
        所有字段用 d.get(键, 默认值) 兜底，防止旧文件缺字段时 KeyError。
        """
        return cls(
            name=d.get("name", ""),
            age=d.get("age", 0),
            sex=d.get("sex", ""),
            phone=d.get("phone", ""),
            note=d.get("note", ""),
        )
