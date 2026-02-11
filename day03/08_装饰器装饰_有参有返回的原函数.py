"""
案例: 装饰器装饰_有参有返回的原函数

细节:
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致,
    即: 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的.
        原函数有参有返回的, 则 装饰器的内部函数也必须是 有参有返回的.
"""


# 需求: 定义有参有返回值的 get_sum()求和函数, 在不改变其代码的基础上, 添加友好提示: 正在努力计算中...
# 1. 定义装饰器.
def my_decorator(fn_name):
    #内部函数和被装饰函数形式保持一致
    def fn_inner(a,b):
        print("正在努力计算中...")
        return fn_name(a,b)#引用
    return fn_inner

@my_decorator
def get_sum(a,b):
    return a+b

#传统方式
de_get_sum = my_decorator(get_sum)
sum = de_get_sum(10,20)
print(sum)

#函数式方式
sum = get_sum(10,20)
print(sum)
