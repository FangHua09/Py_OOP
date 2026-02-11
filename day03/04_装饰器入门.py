"""
案例: 装饰器入门.

装饰器介绍:
    概述/作用:
        它的本质是1个闭包函数, 目的是 在不改变原有函数的基础上, 对其功能做增强.
        大白话: 装修队 在不改变房屋结构的情况下, 对房屋做装饰(功能增强)
    前提条件:
        1. 有嵌套.
        2. 有引用.
        3. 有返回.
        4. 有额外功能.
    装饰器的用法:
        格式1: 传统写法.
            装饰后的函数名 = 装饰器名(被装饰的原函数名)
            装饰后的函数名()

        格式2: 语法糖.
            在要被装饰的原函数上, 直接写 @装饰器名, 之后直接调用原函数即可.
"""
# 需求: 在发表评论前, 都是需要先登录的.

# 1.定义外部函数, 形参列表接收 要被装饰的函数名(对象)
def login_required(fn_name):
    def fn_inner():
        print("登录成功")#额外逻辑
        fn_name()
    return fn_inner

def comment():
    print("发表评论")

@login_required# 底层其实是: payment = check_login(payment)
def payment():
    print('充值中...')

z_comment = login_required(comment)

if __name__ == '__main__':
    payment()#登录成功  充值中...

    z_comment()#登录成功  发表评论
