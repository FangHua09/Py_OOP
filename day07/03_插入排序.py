"""
案例: 演示插入排序.

插入排序介绍:
    原理:
       把列表分成两部分, 假设第1个元素是有序的, 剩下的元素是无序的, 每次都从无序列表中获取1个元素, 和它前边所有元素比较, 决定它的位置, 进行插入.
       直至无序列表的元素操作完毕, 剩下的列表就是: 有序的.

    流程: 假设共 5 个元素
           第几轮(索引)         该轮比较的总次数         公式(具体的谁和谁比较)
            第1轮(1):            1次                    索引1和 0比较
            第2轮(2):            2次                    索引2和1, 2和0比较
            第3轮(3):            3次                    索引3和2, 3和1, 3和0比较
            第4轮(4):            4次                    索引4和3, 4和2, 4和1, 4和0比较
    要点:
       1. 比较的总轮数.        列表长度 - 1       range(1, n)
       2. 每轮比较的总次数.     range(i, 0, -1)
       3. 谁和谁比较.          索引j 和 j - 1 位置的元素比较
    时间复杂度:
        最优: O(n)
        最坏: O(n²)
    扩展:
        插入排序 = 稳定 排序算法
"""

def insert_sort(list_num):
    n = len(list_num)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if list_num[j] < list_num[j - 1]:
                list_num[j], list_num[j - 1] = list_num[j - 1], list_num[j]
            else:
                break
    return list_num

if __name__ == '__main__':
    list_num = [5, 4, 3, 2, 1]
    print(insert_sort(list_num))