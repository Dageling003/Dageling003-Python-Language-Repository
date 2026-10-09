"""
综合题三：带参数的权限装饰器
需求：写带参数的装饰器 require_role(role)：
- 被装饰函数只有在角色为 admin 时才正常执行
- 否则打印「权限不足，拒绝访问」，且不执行原函数
- 用 @require_role("admin") 和 @require_role("guest") 分别装饰验证
动手前先想清楚：这个装饰器一共几层？每一层分别负责收什么？写反了会报什么错？
"""
def require_role(role):
    """第一层：接收装饰器参数"""
    def decorator(func):
        """第二层：接收被装饰的函数"""
        def wrapper(*args, **kwargs):
            """第三层：接收原函数参数，做权限校验"""
            if role == "admin":
                return func(*args, **kwargs)
            else:
                print("权限不足，拒绝访问")
                # 不执行原函数，也不返回任何值（或者返回 None）
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user_id):
    print(f"管理员成功删除用户 {user_id}")

@require_role("guest")
def view_report():
    print("查看报告内容")

# 输出：管理员成功删除用户 1001
delete_user(1001)

# 输出：权限不足，拒绝访问
view_report()
