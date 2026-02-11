"""
案例: 演示多继承.

需求: 小明是个爱学习的好孩子，想学习更多的摊煎饼果子技术，于是，在百度搜索到黑马程序员学校，报班来培训学习摊煎饼果子技术。

扩展: MRO机制.
    解释:
        Python中有MRO机制, 可以查看某个对象, 在调用函数时的 顺序, 即: 先找哪个类, 后找哪个类.
    格式:
        类名.mro()
        类名.__mro__

"""


# ctrl+z: 撤回刚刚的操作
# 1. 定义师傅类.
class Master:
    # 1.1 定义师傅类属性.
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    # 1.2 定义师傅类方法.
    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')


# 2. 定义黑马学校类.
class School:
    # 2.1 定义学校类属性.
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    # 2.2 定义学校类方法.
    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')


# 3.定义徒弟类 -> 有个对象叫 小明.
class Prentice(School, Master):
    pass

#假如左侧的父类没有，那就从左往右找
xm = Prentice()
xm.make_cake()
print(xm.kongfu)

## 5. 查看mro机制的结果.两种查看方法，
print(Prentice.mro())
print(Prentice.__mro__)
#(<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)
#MRO：method resolution order方法解析顺序