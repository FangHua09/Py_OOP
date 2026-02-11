"""
案例: 继承入门.


继承介绍:
    概述:
        大白话: 子承父业.
        专业版: 子类可以继承父类的属性 和 行为.
    写法:
        class 子类名(父类名):
            pass
    例如:
        class A(B):
            pass
    叫法:
        A: 子类, 派生类
        B: 父类, 基类, 超类
    好处:
        提高代码的复用性
    弊端:
        耦合性增强了, 父类不好的内容, 子类想没有都不行.
    扩展: 开发原则
        高内聚, 低耦合.
        内聚: 指的是类自己独立处理问题的能力.
        耦合: 指的是类与类之间的关系.
        大白话解释: 自己能搞定的事儿, 就不要麻烦别人.
"""

# 需求: 定义父类(男, 散步), 定义子类, 继承父类.
# 1. 定义父类.
class Father:
    def walk(self):
        print("散步")

    def smoking(self):
        print("抽烟")

    def drink(self):
        print("喝酒")

    def __init__(self):
        print("父类初始化")

    def __str__(self):
        return f"性别是: {self.gender}"

    gender = "男"
# 2. 定义子类.
class Son(Father):
    pass

s1 = Son()
print(s1)
s1.drink()
s1.smoking()
s1.walk()

