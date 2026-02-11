"""
案例: 装饰器装饰_有参有返回的原函数

细节:
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致,
    即: 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的.
        原函数有参有返回的, 则 装饰器的内部函数也必须是 有参有返回的.
"""


# 需求: 定义1个可以计算多个数据和字典value值和的函数, 并给其友好提示.
# 1. 定义装饰器.
def my_decorator(fn_name):
    #内部函数和被装饰函数形式保持一致
    def fn_inner(*args,**kwargs):
        print("正在努力计算中...")
        return fn_name(*args,**kwargs)#引用
    return fn_inner

# @my_decorator
# def get_sum(*args,**kwargs):
#     Sum = 0
#     for i in args:
#         Sum += i
#
#     for i in kwargs.values():
#         Sum += i
#
#     return  Sum

@my_decorator
def get_sum(*args,**kwargs):
    return sum(args)+sum(kwargs.values())

#传统
# de_get_sum = my_decorator(get_sum)
# Sum = de_get_sum(10,20,30,a=10,b=20)
# print( Sum)

#函数式
Sum = get_sum(10, 20, 30, a=10, b=20)
print(Sum)