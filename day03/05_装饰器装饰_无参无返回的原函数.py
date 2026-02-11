"""
案例: 装饰器装饰_无参无返回的原函数

细节:
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致,
    即: 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的.
        原函数有参有返回的, 则 装饰器的内部函数也必须是 有参有返回的.
"""

# 需求: 定义无参无返回值的 get_sum()求和函数, 在不改变其代码的基础上, 添加友好提示: 正在努力计算中...
# 1. 定义装饰器.
def my_decorator(fn_name):
    def fn_inner():
        print("努力计算中，，，")
        fn_name()#引用
    return fn_inner

@my_decorator
def get_sum():
    a=10
    b=20
    print(f'和为:{a+b}')

#传统
de_get_sum = my_decorator(get_sum)
de_get_sum()

#语法糖
get_sum()