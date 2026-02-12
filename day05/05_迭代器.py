"""
案例: 演示自定义迭代器.

迭代器介绍:
    概述:
        自定义的类, 只要重写了 __iter__() 和 __next__() 方法, 就可以称为 迭代器.
    目的:
        隐藏底层的逻辑, 让用户使用更方便.
        惰性加载, 用的时候才会获取.

回顾: for循环格式
    for i in 可迭代类型:
        pass
"""
# 需求: 模拟range(1, 6), 自定义 迭代器实现同等逻辑.
# 场景1: 回顾 range()用法.
for i in range(1, 6):
    print(i)
print('-' * 23)

# 场景2: 自定义迭代器.
# 1. 自定义 迭代器类.
class MyIterator:
    def __init__(self, start, end):
        self.current_value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):#指向下一个索引，返回当前值
        if self.current_value > self.end:
            raise StopIteration
        else:
            self.current_value += 1
            return self.current_value - 1

for i in MyIterator(1, 5):
    print(i)
    #next（）函数遍历

print('---------------------------')

my_itr  = MyIterator(1, 5)
print(next(my_itr))#1
print(next(my_itr))#2
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))#StopIteration