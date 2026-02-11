"""
案例: 演示在类外 如何获取 和 设置 对象的属性.

类外, 设置对象的属性, 格式如下:
    对象名.属性名 = 属性值
    特点: 该属性独属于这个对象, 即: 该类的其它对象没有这个属性.

类外, 获取对象的属性, 格式如下:
    对象名.属性名
"""

# 需求: 创建汽车类, 设置为红色, 4个轮胎, 有跑的功能.
# 1.创建汽车类.
class Car:
    #属性
    color = "红色"
    tire = 4

    #行为
    def run(self):
        print('汽车会跑...')
    def showColor(self):
        print(f'汽车颜色是: {self.color}')
    def showTire(self):
        print(f'汽车轮胎数是: {self.tire}')

#2.创建汽车对象.
c1 = Car()
c1.run()
print(f"汽车的颜色是: {c1.color}，汽车的轮胎数是: {c1.tire}")

#属性也可以类外修改或者创建
c1.color = "蓝色"
c1.tire = 6
print(f"汽车颜色是: {c1.color}，汽车轮胎数是: {c1.tire}")

c1.brand="benz"
print(f"汽车品牌是: {c1.brand}")

#栈存放实例对象指向堆，堆存放每个实例对象的属性。方法区存放类中共有的方法，并用self传相应的参数

