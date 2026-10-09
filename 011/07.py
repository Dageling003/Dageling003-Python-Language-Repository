"""
综合题七：函数执行审计器
- 写一个带参数的装饰器 audit(mode)：mode 为 full 时打印函数名 + 参数 + 返回值；mode 为 simple 时只打印函数名
- 用它装饰一个 add_user(info) 函数，info 是字典，里面带嵌套列表
- add_user 内部先把 info深拷贝一份再处理，返回处理后的新字典
- 处理逻辑自定（比如给新用户加默认等级、往嵌套列表里追加一个默认技能）
自测：
1. 同一个函数换 mode 装饰两次，打印内容随 mode 变化
2. 返回的新字典与传入的字典完全独立——随便改其中一个，另一个不受影响（用打印验证）
"""
import copy
from functools import wraps

def audit(mode):
    """第一层：接收装饰器参数"""
    def decorator(func):
        """第二层：接收被装饰的函数"""
        @wraps(func)  # 保留原函数的元信息（如 __name__、__doc__）
        def wrapper(*args, **kwargs):
            """第三层：接收原函数参数，做权限校验"""
            if mode == 'full':
                print(f"[AUDIT FULL] 函数名：{func.__name__}")
                print(f"参数：args={args},kwargs={kwargs}")
            elif mode == 'simple':
                print(f"AUDIT SIMPLE] 函数名: {func.__name__}")
            else:
                raise ValueError(f"未知的 audit mode: {mode}")
            # 执行原函数
            result = func(*args, **kwargs)

            if mode == 'full':
                print(f"  返回值: {result}")
            return result
        return wrapper
    return decorator

def add_user(info):
    """
        处理用户信息：深拷贝后添加默认等级和默认技能。
        info 示例：{'name': 'Alice', 'skills': ['python', 'java']}
        """
    new_info = copy.deepcopy(info)
    new_info.setdefault('level',1)
    skills = new_info.get('skills')
    if skills is not None and isinstance(skills, list):
        skills.append('basic_attack')  # 往嵌套列表追加默认技能
    else:
        new_info['skills'] = ['basic_attack']
    return new_info

# 原始函数（未装饰）
original_add_user = add_user

# 用 full 模式装饰
add_user_full = audit('full')(original_add_user)

# 用 simple 模式装饰
add_user_simple = audit('simple')(original_add_user)

# 测试数据
test_info = {'name': 'Bob', 'skills': ['C++']}

print("=== 测试 full 模式 ===")
result_full = add_user_full(test_info)
print()

print("=== 测试 simple 模式 ===")
result_simple = add_user_simple(test_info)
print()

print("\n=== 测试独立性 ===")
original = {'name': 'Eve', 'skills': ['go']}
new_dict = add_user_full(original)   # 此时 original 未被修改

print("原始字典:", original)
print("新字典:", new_dict)

# 修改原始字典
original['name'] = 'Eve_modified'
original['skills'].append('rust')

print("\n修改原始字典后：")
print("原始字典:", original)
print("新字典:", new_dict)           # 新字典应保持不变

# 修改新字典
new_dict['name'] = 'New_Eve'
new_dict['skills'].append('haskell')

print("\n修改新字典后：")
print("原始字典:", original)
print("新字典:", new_dict)
