import time

from Student import Student


class StudentCMS(object):
    """
    学生管理系统类，用于管理学生信息。

    属性:
        stu_list (list): 存储学生对象的列表。
    """

    def __init__(self):
        """
        初始化学生管理系统，创建一个空的学生列表。
        """
        self.stu_list = []

    # 因为该函数中没有使用self, 所以可以把该函数定义为静态方法.
    @staticmethod
    def show_view():
        """
        显示学生管理系统的主菜单界面。
        该方法为静态方法，不依赖于类的实例。
        """
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*' * 23)

    def add_student(self):
        """
        添加学生信息到系统中。
        具体实现待补充。
        """
        name = input('请输入学生姓名：')
        gender = input('请输入学生性别：')
        age = input('请输入学生年龄：')
        phone = input('请输入学生手机号：')
        desc = input('请输入学生描述：')
        self.stu_list.append(Student(name, gender, age, phone, desc))
        print(f'学生：{name} 添加成功！')

    def del_student(self):
        """
        从系统中删除指定学生信息。
        具体实现待补充。
        """
        name = input('请输入要删除的学生姓名：')
        for i in self.stu_list:
            if i.name == name:
                self.stu_list.remove(i)
                print(f'学生：{name} 删除成功！')
                return
        print("查无此人")

    def update_student(self):
        """
        修改系统中的学生信息。
        具体实现待补充。
        """
        upd_name = input("请输入要修改的学生姓名：")
        for i in self.stu_list:
            if i.name == upd_name:
                i.name = input("请输入学生姓名：")
                i.age = input("请输入学生年龄：")
                i.gender = input("请输入学生性别：")
                i.phone = input("请输入学生手机号：")
                i.desc = input("请输入学生描述：")
                print(f'{upd_name} 修改成功！')
                return
        print("没有此学生！")


    def search_one_student(self):
        """
        查询单个学生的信息。
        具体实现待补充。
        """
        name = input("请输入学生姓名：")
        for i in self.stu_list:
            if i.name == name:
                print(i)
                return
        print("没有此学生！")

    def search_all_student(self):
        """
        查询所有学生的信息。
        具体实现待补充。
        """
        if len(self.stu_list) == 0:
            print("没有学生信息！")

        for i in self.stu_list:
            print(i)
        print("查询完毕！")

    def save_student(self):
        """
        将学生信息保存到文件或数据库中。
        具体实现待补充。
        """
        with open('stu_data.txt','w',encoding= 'utf-8') as f:
            stu_dict = [i.__dict__ for i in self.stu_list]
            f.write(str(stu_dict))


    def load_student(self):
        """
        从文件或数据库中加载学生信息到系统中。
        具体实现待补充。
        """
        try:
            with open('stu_data.txt','r',encoding= 'utf-8') as f:
                stu_dict = f.read()
                stu_list = eval(stu_dict)  # 将字符串转换成列表,去除两边单引号
                if len(stu_list) == 0:
                    stu_list = []
                self.stu_list = [Student(**stu) for stu in stu_list]
        except:
            with open('stu_data.txt','w',encoding= 'utf-8') as f:
                f.write('[]')
            pass

    def start(self):
        """
        启动学生管理系统，进入主循环。
        具体实现待补充。
        """
        self.load_student()
        while True:
            # 11.3 为了效果更明显, 加入: 延迟(休眠线程)
            time.sleep(1)
            # 11.4 打印 学生管理系统的界面.
            StudentCMS.show_view()
            # 11.5 提示用户录入要操作的编号, 并接收.
            input_num = input('请输入您要操作的编号:')
            # 11.6 根据用户输入的编号, 做不同的操作.
            if input_num == '1':
                # 添加学生信息
                # print('添加学生信息\n')
                self.add_student()
            elif input_num == '2':
                # 删除学生信息
                # print('删除学生信息\n')
                self.del_student()
            elif input_num == '3':
                # 修改学生信息
                # print('修改学生信息\n')
                self.update_student()
            elif input_num == '4':
                # 查询单个学生信息
                # print('查询单个学生信息\n')
                self.search_one_student()
            elif input_num == '5':
                # 查询所有学生信息
                # print('查询所有学生信息\n')
                self.search_all_student()
            elif input_num == '6':
                # 保存学生信息
                self.save_student()
                print('保存学生信息成功!\n')
            elif input_num == '0':
                # 退出系统, 做二次校验.
                result = input('您确定要退出吗? (Y/N) -> ')
                if result.lower() == 'y':  # 字符串的lower() -> 把字母转成小写形式.
                    # 在退出前, 自动保存学生数据到文件.
                    self.save_student()
                    print('谢谢您的使用, 期待下次再会!')
                    break
            else:
                # 输入错误
                print('录入有误, 请重新录入!\n')


if __name__ == '__main__':
    cms=StudentCMS()
    cms.start()