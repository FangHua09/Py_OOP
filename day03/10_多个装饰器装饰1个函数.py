"""
案例: 演示多个装饰器装饰1个函数.

记忆:
    多个装饰器装饰1个原函数, 是按照 由内向外的顺序来装饰的,
    但如果你要是用 装饰器的写法来做, 看到的效果是: 从上往下执行的.

装饰器语法糖（@）的执行顺序是自下而上（离函数近的先包装）。
手动调用装饰器的赋值语句是自上而下（写在前面的先执行）。

想要手动写法和语法糖效果一致，必须颠倒手动赋值的书写顺序（先写内层装饰器的调用，再写外层），才能匹配语法糖 “自下而上” 的包装逻辑。
"""

# 需求: 发表评论前, 需要先登录, 在验证验证码. 请用所学, 模拟该功能.
# 1. 定义装饰器, 表示: 登录
def login_decorator(fn_name):
    def fn_inner():
        print("登录成功")
        fn_name()
    return fn_inner

#2，定义装饰器，表示：验证码
def check_code_decorator(fn_name):
    def fn_inner():
        print("验证码验证成功")
        fn_name()
    return fn_inner

# @check_code_decorator # 外层装饰器（后执行包装）
# @login_decorator # 内层装饰器（先执行包装）
def publish_comment():
    print("发表评论成功")
# 4. 测试.
# 4.1 传统写法.
comment = check_code_decorator(publish_comment) # 第一步：先包装check_code
comment = login_decorator(comment)# 第二步：再包装login
comment()

print("-----------------")

# publish_comment()

"""
传统：
登录成功
验证码验证成功
发表评论成功
-----------------
-----------------
优化版：由内向外装饰，由外向内解装饰
验证码验证成功
登录成功
发表评论成功

"""

