"""
案例: 创建类的格式介绍.


格式1:
    class 类名:
        pass

格式2:
    class 类名():
        pass

格式3:
    # class 类名(父类名):
    class 类名(object):
        pass
"""

# 需求: 定义老师类
class Teacher( object):
    pass

class Math_Teacher(Teacher):
    pass

t1 = Teacher()
print(t1)

s1=Math_Teacher()
print(s1)