"""
综合题六：深浅拷贝排查
场景：你要写一个函数 new_profile(name)，给每个用户生成一份「用户配置」：
- 配置包含基础信息（姓名、等级）和一个嵌套的技能列表 skills
- 你用 b = a.copy() 给第二个用户生成配置，然后修改第二个用户的 skills，结果第一个用户的 skills 也跟着变了
要求按三步走：
1. 先写出这段「会出问题」的代码，运行复现问题
2. 说明原因：到底是哪一层被共享了？copy() 到底复制了什么、没复制什么？
3. 用两种方式分别修复：换拷贝方式；或者改成每次生成配置时都新建嵌套对象
自测：修复后，两个用户的 skills 修改互不影响。
"""
import copy
def new_profile(name):
    profile = {
        "name": name,
        "level": 1,
        "skills": ["Python", "Git"]
    }
    return profile

p1 = new_profile("Alice")
p2 = p1.copy()
p2["skills"].append("Docker")
print(p1["skills"])
print(p2["skills"])
"""
基本的方法运行的结果：
['Python', 'Git', 'Docker']
['Python', 'Git', 'Docker']

问与思考（要有答）：
1、p1.copy() 复制了什么？它是深拷贝还是浅拷贝？
答：p1.copy() 是浅拷贝。它复制了字典本身（创建了一个新的字典对象），但字典
中的值（如 skills 列表）只是复制了它们的引用，并没有递归复制嵌套的可变对象。
2、p1 和 p2 的 skills 键对应的值是什么关系？它们在内存中是同一个对象还是两个独立的对象？
答：它们是同一个对象。p1["skills"] 和 p2["skills"] 指向内存中同一个列表，因此 id() 相同。
3、为什么修改 p2["skills"] 会影响到 p1["skills"]？
答：因为浅拷贝只复制了列表的引用，没有创建新列表。p2["skills"].append("Docker") 
是在原列表对象上直接修改，所以 p1["skills"] 看到的也是修改后的同一个列表。
比如【测试下面代码】：用 id() 函数来验证两个对象的 skills 是否为同一对象
print(id(p1["skills"]))
print(id(p2["skills"]))

测试结果：
1761280296064
1761280296064
"""
print(id(p1["skills"]))
print(id(p2["skills"]))

"""
解决方案
方法1、使用深拷贝 copy.deepcopy()
开头加一个import copy;

p2 = p1.copy()   原来代码改成 p2 = copy.deepcopy(p1)
"""
p2 = copy.deepcopy(p1)
# 测试
p2["skills"].append("Docker Compose")
print(p2["skills"])

"""
方法2：每次生成配置时新建嵌套对象
在 new_profile 函数内部，每次返回一个新创建的 skills 列表（而不是复用同一个默认列表）。例如：

def new_profile(name):
    profile = {
        "name": name,
        "level": 1,
        "skills": ["Python", "Git"]   # 每次调用都会新建一个列表
    }
    return profile
"""




