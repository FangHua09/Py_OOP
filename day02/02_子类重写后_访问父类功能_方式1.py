"""
案例: 子类重写父类功能后, 继续访问父类功能.

思路:
    1. 父类名.父类函数名(self)      精准访问, 想找哪个父类, 就调哪个父类.
    2. super().父类函数名()        只能访问最近的那个父类, 有就用, 没有就往后继续查找.
"""


# 故事4: 很多顾客都希望能吃到徒弟做出的有自己独立品牌的煎饼果子，也有黑马配方技术的煎饼果子味道。
# 1. 老师父类
class Master:
    # 1.1 属性
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    # 1.2 行为
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 黑马学校类
class School:
    # 2.1 属性
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    # 2.2 行为
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 3. 徒弟类
class Prentice(School, Master):
    def __init__(self):
        super().__init__()  # 子类必须调用父类的初始化方法，确保父类有属性
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    # 调用不同父类的功能
    def make_master_cake(self):
        Master.__init__(self)  # 将self传进去，让特定父类的属性赋给传入self（自己）的属性
        Master.make_cake(self)  # 调用Master的方法

    def make_school_cake(self):
        School.__init__(self)  ##将self传进去，让特定父类的属性赋给传入self（自己）的属性
        School.make_cake(self)  # 调用School的方法


if __name__ == '__main__':
    p = Prentice()
    p.make_cake()
    p.make_master_cake()
    p.make_school_cake()
    """
    假如没有写主类名.__init__(self)
运用[独创煎饼果子配方]制作煎饼果子
运用[独创煎饼果子配方]制作煎饼果子
运用[独创煎饼果子配方]制作煎饼果子
    """
