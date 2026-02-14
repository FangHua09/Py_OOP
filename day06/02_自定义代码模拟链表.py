"""
案例: 自定义代码模拟链表

链表介绍:
    概述:
        它属于数据结构之 线性结构的一种, 每个节点都只能有 1个前驱 和 1个后继节点.
    作用:
        用于优化顺序表的弊端(如果没有足够的连续的内存空间, 会导致扩容失败)
        链表扩容时, 有地儿就行, 连不连续无所谓.
    组成:
        由 节点 组成, 其中节点由 元素域(数值域) 和 链接域(地址域)组成.
    分类:
        根据 节点类型不同, 链表主要分为:
        单向链表: 节点由1个数值域 和 1个地址域组成, 前边节点的地址域存储的是后续节点的地址, 最后1个节点的地址域为 None
        单向循环链表:
        双向链表:
        双向循环链表:
        详见今日随堂图片.

自定义代码模拟链表, 思路分析:
    1. 自定义SingleNode类, 表示 节点类.
        属性:
            item   数值域(元素域)
            next   地址域(链接域)

    2. 自定义SingleLinkedList类, 表示: 链表
        属性:
            head  表示头结点, 指向第1个节点.
        行为:
            is_empty(self) 链表是否为空
            length(self) 链表长度
            travel(self. ) 遍历整个链表
            add(self, item) 链表头部添加元素
            append(self, item) 链表尾部添加元素
            insert(self, pos, item) 指定位置添加元素
            remove(self, item) 删除节点
            search(self, item) 查找节点是否存在

    3. 测试.
"""

# 1. 自定义SingleNode类, 表示 节点类.
class SingleNode(object):
    def __init__(self,item):
        self.item = item
        self.next = None

# 2. 自定义SingleLinkedList类,
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    # 链表是否为空
    def is_empty(self):
        return self.head is None

    # 链表长度
    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return  count

    # 遍历整个链表
    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next

    # 链表头部添加元素
    def add(self,item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node
        print('添加成功!')

    # 链表尾部添加元素
    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
            print('添加成功!')
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            print('添加成功!')

    # 指定位置添加元素
    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < pos - 1:#移动pos-1次，到达插入位置的前一个节点
                count += 1
                pre = pre.next
            new_node = SingleNode(item)
            new_node.next = pre.next#先指向前一个节点的原next（即后一个节点），再指向新节点
            pre.next = new_node
            print('添加成功!')

    # 删除节点
    def remove(self,item):
        cur = self.head#移动cur，到达要删除的节点
        pre = None#记录要删除节点的前一个节点
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                print('删除成功!')
                return
            else:
                pre = cur
                cur = cur.next
        print('未找到该元素!')

    # 查找节点是否存在
    def search(self,item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    linked_list = SingleLinkedList()
    linked_list.add(1)#1
    linked_list.append(2)#1 2
    linked_list.insert(1,3)#插入3。结果1 3 2
    linked_list.travel()#1 3 2
    print(linked_list.length())#3
    linked_list.remove(3) #删除3。结果1 2

    print(linked_list.travel())

    print(linked_list.search(2))# True
    print(linked_list.search(3))# False

    print('--------------------------')
    #假如索引负数以及大于列表长度的插入
    linked_list.insert(-1,4)
    linked_list.insert(5,5)
    linked_list.travel()#4 1 2 5

    #删除不存在的元素
    print()
    linked_list.remove(6)#4 1 2 5
    linked_list.travel()

    print()
    linked_list.remove(4)#1 2 5
    linked_list.travel()

    print()
    linked_list.remove(1)
    linked_list.travel()#2 5