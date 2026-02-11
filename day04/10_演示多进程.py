"""
案例: 演示多进程入门案例.

多进程目的:
    它属于多任务的一种实现方式, 目的是充分利用CPU资源, 提高程序执行效率.

实现方式:
    1. 导包.
    2. 创建进程对象, 关联目标函数.
    3. 启动进程.

子进程对象 =multiprocessing.Process (group=None, target=None, name=None, args=(), kwargs={})
group — 参数未使用，值始终为 None
target — 表示调用对象，即子进程要执行的任务（回调函数入口地址）
args — 表示以元组的形式向子任务函数传参，元组方式传参一定要和参数的顺序保持一致
kwargs — 表示以字典的方式给子任务函数传参，字典方式传参字典中的 key 要和参数名保持一致
name — 为子进程的名称
"""

# 导包
import multiprocessing
import time
# 1. 定义函数 表示 编写代码.
def coding():
    for i in range(1, 11):
        time.sleep(0.1) # 可以模拟耗时操作, 更好的查看多任务的执行效果.
        print(f'正在敲第 {i} 遍代码!')


# 2. 定义函数 表示 听音乐。
def music():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f'正在听第 {i} 遍音乐......')


# 3. 创建两个进程对象, 分别关联上述的两个 目标函数.
# 细节: 通过main进程(主进程)来创建子进程.
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)
    p1.start()
    p2.start()