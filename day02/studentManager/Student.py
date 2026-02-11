"""
该文件用于记录 学生类, 学生的属性信息为: 姓名, 性别, 年龄, 手机号, 描述信息.
"""

# 1. 定义学生类.
class Student:
    # 2. 定义魔法方法, 初始化属性信息.
    def __init__(self, name, gender, age, phone, desc):
        """
        该魔法方法用于初始化属性信息
        :param name: 学生姓名
        :param gender:  性别
        :param age: 年龄
        :param phone: 手机号
        :param desc: 描述
        """
        self.name = name
        self.gender = gender
        self.age = int( age)
        self.phone = phone
        self.desc=desc

    def __str__(self):
        """
        打印 信息
        :return:
        """
        return '姓名: %s, 性别: %s, 年龄: %d, 手机号: %s, 描述: %s' % (self.name, self.gender, self.age, self.phone, self.desc)


# 4. 测试
if __name__ == '__main__':
    s = Student('乔峰', '男', 38, '13112345678', '丐帮帮主')
    print(s)
