"""
案例: 演示多态入门.

多态概述:
    专业版: 同一个函数, 接收不同的参数, 有不同的效果
    大白话: 同一个事物在不同时刻表现出来的不同状态, 形态.

    前提条件:
        1. 要有继承.
        2. 要有方法重写, 不然多态无意义.
        3. 要有父类引用指向子类对象.
    案例:
        动物类案例.
"""
# 1.定义动物类
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

# 汽车类
class Car:
    def speak(self):
        print('车叫: 滴滴滴')

# 4. 定义函数, 接收不同的动物对象, 调用speak方法
def make_noise(an: Animal):  # an:Animal = Dog()
        an.speak()#父类引用指向子类对象

if __name__ == '__main__':
    # 创建对象
    cat = Cat()
    dog = Dog()

    make_noise( cat)
    make_noise( dog)




