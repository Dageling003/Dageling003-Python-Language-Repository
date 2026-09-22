"""
3. 定义 apply(lst, func) 对列表每个元素应用 func，用 lambda 把 [1,2,3] 变成 [2,4,6]。
"""
def apply(lst,func):
    return [func(x) for x in lst]

result =apply([1,2,3],lambda x:x*2)
print(result)
