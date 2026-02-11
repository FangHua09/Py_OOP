"""
案例: 减肥案例.

需求:
    例如，小明同学当前体重是100kg。每当他跑步一次时，则会减少0.5kg；每当他大吃大喝一次时，则会增加2kg。请试着采用面向对象方式完成案例。

分析:
    类名:         Student
    对象名:        xm
    属性(名词):   当前体重, current_weight
    行为(动词)    跑步, 吃饭
"""
class Student:
    # 属性
    name=None
    current_weight=None
    # 行为
    def __init__(self,name,current_weight):
        self.name=name
        self.current_weight=current_weight

    def run(self):
        self.current_weight-=0.5
        print(f"{self.name}正在跑步，当前体重为{self.current_weight}kg")

    def eat(self):
        self.current_weight+=2
        print(f"{self.name}正在吃东西，当前体重为{self.current_weight}kg")

    def show(self):
        print(f"{self.name}的当前体重为{self.current_weight}kg")

Student1=Student("小明",100)
Student1.run()
Student1.eat()
Student1.run()
Student1.run()
Student1.run()

Student1.show()

