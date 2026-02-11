"""
案例: 装饰器装饰_有参无返回的原函数

细节:
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致,
    即: 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的.
        原函数有参有返回的, 则 装饰器的内部函数也必须是 有参有返回的.
"""


# 需求: 定义无参有返回值的 get_sum()求和函数, 在不改变其代码的基础上, 添加友好提示: 正在努力计算中...
# 1. 定义装饰器.
def my_decorator(fn_name):
    # 内部函数和被装饰函数形式保持一致，即被装饰函数有返回，内部函数也有返回
    def fn_inner():
        print("正在努力计算中...")
        return fn_name()

    return fn_inner

@my_decorator
def get_sum():
    a = 10
    b = 20
    return a + b

# 传统
de_get_sum = my_decorator(get_sum)
print(de_get_sum())

# 函数式
get_sum()
