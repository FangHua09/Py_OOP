"""
案例: 演示多线程特点之 守护线程.

多线程特点:
    1. 线程执行具有随机性, 原因是因为CPU在做着高效的切换.
    2. 默认情况下, 主线程会等待子线程结束再结束.
    3. (同一个进程的)线程间 数据共享。
    4. 多线程操作共享数据， 可能会出现安全问题， 可以用 互斥锁解决。

"""
# 导包
import threading, time

# 1.定义目标函数.
def work():
    for i in range(10):
        time.sleep(0.2)
        print('工作中...')

if __name__ == '__main__':
    t = threading.Thread(target=work)
    t.daemon = True
    t.start()
    time.sleep(1)
    print('主线程结束')