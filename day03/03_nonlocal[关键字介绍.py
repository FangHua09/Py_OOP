"""
案例: nonlocal关键字介绍

nonlocal:
    它是Python内置的关键字, 可以实现 在内部函数中 修改外部函数的 变量值.
"""


# 需求: 编写1个闭包,让内部函数访问外部函数的参数 a = 100, 并观察结果.
# 1. 定义外部函数.
def fu_outer():
    a = 100

    def fu_inner():
        nonlocal a
        a+=1
        print(f'a:{a}')

    return fu_inner


if __name__ == '__main__':
    fu_inner = fu_outer()
    fu_inner()
    fu_inner()
    fu_inner()
    fu_inner()
    """
    a:101
    a:102
    a:103
    a:104
    """
"""
第一步：执行 fu_outer() 时的内存变化
栈：创建 fu_outer 的栈帧，栈帧中包含局部变量 a = 100（此时 a 是栈帧内的普通局部变量）。
方法区：fu_outer 和 fu_inner 的函数字节码、定义信息早已存在（程序启动时加载）。
关键：当 fu_outer 定义 fu_inner 并返回它时，fu_inner 作为闭包，会把外层的 a 从 fu_outer 的栈帧中 “捕获” 到堆内存中（而不是随栈帧销毁）。
第二步：nonlocal a 的核心作用
如果没有 nonlocal a：
执行 fu_inner() 时，栈会创建 fu_inner 的栈帧，代码里的 a += 1 会被解释器认为是 “定义局部变量 a”，但 a 还没赋值就做加法，会直接报错（UnboundLocalError）。
加上 nonlocal a 后：
解释器会明确：fu_inner 中的 a 不是当前栈帧的局部变量，而是 “上一级非全局的、被闭包捕获到堆里的 a”。
简单说：nonlocal 告诉解释器 ——“去堆里找外层函数的 a，不要在当前栈帧里新建 a”。
第三步：多次调用 fu_inner() 的内存逻辑
plaintext
# 第一次调用 fu_inner()
栈：创建 fu_inner 栈帧 → 通过 nonlocal 找到堆里的 a=100 → a +=1 → 堆里的 a 变成 101 → 打印 → 栈帧销毁
# 第二次调用 fu_inner()
栈：创建新的 fu_inner 栈帧 → 再次通过 nonlocal 找到堆里的 a=101 → a +=1 → 堆里的 a 变成 102 → 打印 → 栈帧销毁
# 后续调用逻辑一致，堆里的 a 持续累加
"""