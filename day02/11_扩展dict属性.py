"""
案例: 演示Python内置的dict属性.

__dict__ 属性介绍:
    它是Python内置的属性, 可以把对象转成字典形式.
"""
#从studentManager包中导入Student.py模块，再import类
from studentManager.Student import Student
# 需求1: 把 学生对象 -> 字典形式, 属性名做键, 属性值做值.
s1 = Student('德桦', '男', 81, '111', '刻骨铭心')
print(s1)

# {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'}
my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))
print('-' * 23)

# 需求2: 把 [学生对象, 学生对象, 学生对象] -> [字典, 字典, 字典]
s1 = Student('德桦', '男', 81, '111', '刻骨铭心')
s2 = Student('志奇', '男', 22, '222', '我不是紫琦')
s3 = Student('紫琦', '男', 66, '333', '有请志奇')
#先转成列表
my_list = [s1, s2, s3]

#列表推导式
my_dict_list = [s.__dict__ for s in my_list]
print(my_dict_list)

# 需求3: 把 {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'} -> 学生对象
my_dict = {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'}
s4=Student(my_dict['name'],my_dict['gender'],my_dict['age'],my_dict['phone'],my_dict['desc'])
print(s4)
print(type(s4))
print('-' * 23)

#简单写法
s5 = Student(**my_dict)
print(s5)
print(type(s5))#<class 'studentManager.Student.Student'>