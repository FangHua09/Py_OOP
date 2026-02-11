"""
案例: 演示 带参数的装饰器.

记忆:
    1. 1个装饰器的参数有且只能有 1个.
    2. 如果装饰器有多个参数, 可以在该装饰器的外边再包裹一层, 把该装饰器当作其 内部函数 返回即可.
"""

# 需求: 定义1个既能装饰减法, 又能装饰加法的装饰器 -> 即: 带有参数的装饰器.
# 1. 定义装饰器.
# fn_name: 原函数名.  flag: 标记    报错, 装饰器的参数只能有1个.
# def my_decorator(fn_name, flag):
def logging(flag):
    def my_decorator(fn_name):
        def fn_inner(a,b):
            if flag=='+':
                print('正在努力计算 [加法] 中...')
            elif flag=='-':
                print('正在努力计算 [减法] 中...')
            return fn_name(a,b) # 1.3 有引用.
        return fn_inner # 1.4 有返回.
    return my_decorator # 返回 my_decorator函数.

@logging('+')
def get_sum(a,b):
    return a+b

@logging('-')
def get_sub(a,b):
    return a-b

print(get_sum(10,20))

print(get_sub(10,20))


