"""
案例: 烤地瓜案例.

需求:
    1. 定义地瓜类 -> SweetPotato
    2. 属性: 被烤时间cook_time, 烘焙状态 cook_state, 调料 condiments
    3. 行为: 烘烤cook(), 添加调料 add_condiment()
    4. 魔法方法: init() -> 初始化属性,  str() -> 打印地瓜信息.
    5. 规则:
        烘烤时间        地瓜状态
        [0, 3)          生的          包左不包右, 前闭后开.
        [3, 7)          半生不熟
        [7, 12)         熟了
        [12, ∞]         糊了
"""
# 1. 定义地瓜类 -> SweetPotato
class SweetPotato:
    #行为
    def __init__(self):
        self.state = '生的'
        self.cook_time = 0
        self.condiments = []

    def __str__(self):
        return f'地瓜状态是: {self.state}, 时间是: {self.cook_time}分钟，添加的调料是: {self.condiments}'

    def add_Condiments(self, condiments):
        self.condiments.append(condiments)

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.state = '生的'
        elif 3 <= self.cook_time < 7:
            self.state = '半生不熟'
        elif 7 <= self.cook_time < 12:
            self.state = '熟了'
        elif self.cook_time >= 12:
            self.state = '烤糊了'
        else:
            print('时间输入有误')

# 2. 创建地瓜对象
s1 = SweetPotato()
s1.cook(88)
s1.add_Condiments('辣椒')
s1.add_Condiments('芥末')
s1.add_Condiments('盐')
print(s1)
