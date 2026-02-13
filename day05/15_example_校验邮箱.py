r"""
案例: 演示正则表达式之 校验邮箱.

正则规则:
    |           代表 或者的意思
    ()          代表 分组, 从左往右数, 第几个左小括号(, 就表示第几组
    \num        代表 引用第几组的内容.

    扩展:
        (?P<分组名>)   设置分组
        (?P=分组名)    使用分组
"""
# 导包
import re


# 1. 定义邮箱.
email = "abcd@163.com"

result = re.match(r'^\w{4,20}@(163|qq|gmali)\.com',email)
print(result)

#result.group()：获取匹配结果
print(result.group())
print(result.group(0))#一样效果
print(result.group(1))#获取第一个分组的内容
