"""
案例: 演示property属性的用法.

property属性介绍:
    概述/目的/作用:
        把 函数 当做 变量来使用.
    实现方式:
        方式1: 装饰器.
        方式2: 类属性.


property的装饰器用法:
    @property               修饰 获取值的函数
    @获取值的函数名.setter     修饰 设置值的函数

property类属性的用法:
    类属性名 = property(获取值的函数名, 设置值的函数名)

    之后, 就可以直接 .上述的函数名 来当做变量直接用.
"""


# 需求: 定义学生类, 私有 age属性, 通过property充当类属性用.
# 1. 定义学生类.
class Student:
    def __init__(self):
        self.__age = 18
#为 get_age 和 set_age 方法添加明确的类型注解，帮助类型检查工具理解函数的签名：
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)#顺序必须是：获取值函数名，设置值函数名


if __name__ == '__main__':
    s = Student()
    print(s.age)
    s.age = 20
    print(s.age)
