"""
案例: 定义手机类, 能开机, 关机, 拍照.

回顾:
    定义类的格式
        class 类名:
            # 属性
            # 行为

    访问 类中成员 的格式:
        类外: 对象名. 的方式
        类内: self. 的方式
"""
class Phone:
    #属性

    #行为
    def run(self):
        print("手机开机")

    def close(self):
        print("手机关机")

    def take_Photo(self):
        print("手机拍照")

#创建手机类对象，访问成员
p1 = Phone()
print(f'p1对象: {p1}')
p1.run()
p1.close()
p1.take_Photo()

print('---------------------------------')

p2 = Phone()
print(f'p2对象: {p2}')
p2.run()
p2.close()
p2.take_Photo()

