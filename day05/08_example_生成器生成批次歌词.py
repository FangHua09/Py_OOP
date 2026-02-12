"""
案例: 基于传入的数值(每批次的歌词条数), 创建 生成器, 生成批次歌词.
"""
import math
import sys


# 需求: 基于文件中 周杰伦的歌词, 创建生成器, 根据传入的每批次的歌词条数, 生成歌词批次.
# 1. 定义函数, 接收 每批次的歌词条数, 返回生成器.
def create_generator(batch_size):
    """
    自定义的 歌词 批量生成器
    :param batch_size:  每批次的歌词条数
    :return: 生成器, 每个元素都是一批次的数据, 例如: (8条, 8条, 8条...)
    """
    with open(r'C:\Users\13075\PycharmProjects\Py_OOP\day05\data\jaychou_lyrics.txt', 'r', encoding='utf-8') as src_f:
        lines = [line.strip() for line in src_f.readlines()]

        # 计算批次
        batch_count = math.ceil(len(lines) / batch_size)  # 批次数：上取整
        for i in range(batch_count):
            yield lines[i * batch_size: (i + 1) * batch_size]
# 第1批歌词, 批次索引(idx=0), 歌词为: 第1条 ~ 第8条, 索引为: 0 ~ 7
# 第2批歌词, 批次索引(idx=1), 歌词为: 第9条 ~ 第16条, 索引为: 8 ~ 15
# 第3批歌词, 批次索引(idx=2), 歌词为: 第17条 ~ 第24条, 索引为: 16 ~ 23
print(type(create_generator(8))) #<class 'generator'>
dl = create_generator(4)
print(next(dl))
print(next(dl))
print(next(dl))

# for i in dl:
#     print(i)

print('-------------------------')
print(sys.getsizeof(dl))#单位是字节