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
import sys  # system: 系统模块

# 场景1: 生成器 推导式写法.
# 需求1: 生成1 ~ 10之间的整数.
import sys


# 1. 自定义 迭代器类.
class MyIterator:
    def __init__(self, *args):
        self.current_value = args[0]

    def __iter__(self):
        return self

    def __next__(self):  # 指向下一个索引，返回当前值
        if self.current_value > self.end:
            raise StopIteration
        else:
            self.current_value += 1
            return self.current_value - 1


my_itr = MyIterator(1, 5)
my_generator = (i for i in my_itr)
print(my_generator)
print(type(my_generator))  # <class 'generator'>
print(type(my_itr)) #<class '__main__.MyIterator'>
print('-------------------------------------')

my_gt2 = (i for i in range(1, 11) if i % 2 == 0) #2, 4, 6, 8, 10
print(my_gt2)

print('-------------------------------------')

# 需求3: 如何从生成器中获取数据.
# 思路1: next()
print(next(my_gt2))
print(next(my_gt2))

for i in my_gt2:
    print(i)

print('-------------------------------------')

my_list = [i for i in range(1000000)]
my_generator = (i for i in range(1000000))

print(sys.getsizeof(my_list))#8448728
print(sys.getsizeof(my_generator))#192


