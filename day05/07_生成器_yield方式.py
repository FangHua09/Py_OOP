"""
案例: 演示生成器之 推导式写法.

生成器介绍:
    概述:
        所谓的生成器就是基于 数据规则, 用一部分在生成一部分, 而不是一下子生成完所有.
    目的:
        可以节省大量的内存.
    实现方式:
        1. 推导式写法.
        2. yield关键字
"""

# 需求: 通过yield方式, 获取到生成器之 1 ~ 10之间的整数.
# 回顾: 推导式写法.
my_gt1 = (i for i in range(1, 11))

def fun():
    my_list = [i for i in range(1, 11)]
    return my_list

def fun2():
    for i in range(1, 11):
        yield i # yield在这里做了三件事儿: 1.创建生成器对象.  2.把值存储到生成器中.  3.返回生成器.

my_gt2 = fun2()
print(type(my_gt2))

my_gt3 = fun()
print(type(my_gt3))

#遍历生成器
print(next(my_gt2))
print(next(my_gt2))
print('-------------------------')
for i in my_gt2:
    print(i)