"""
案例: 自定义代码, 模拟二叉树.

树结构解释:
    概述:
        它属于数据结构的一种, 属于 非线性结构(N个前驱, N个后继)
    特点:
        1. 有且只能有1个根节点.
        2. 每个节点都可以有1个父节点 及 任意个子节点, 根节点除外(没有父节点).
        3. 没有子节点的节点, 称之为: 叶子节点.
    常用分类:
        无序树:
        有序树:
        二叉树:
            完全二叉树: 最后一层不满, 其它都是满的.
            满二叉树: 都是满的.
            非完全二叉树: 中间有断的.
            平衡二叉树: 任意节点的两个子树的高度差不超过1

        我们用的最多的就是: 二叉树
    存储:
        顺序存储: 既要存储数据, 又要存储节点的关系.
        链式存储: 采用节点(item, lchild, rchild)的方式, 形成链表来存储

抽取方法的快捷键: ctrl + alt + M
"""
from uuid import main


# 1. 定义Node类, 表示二叉树的节点.
class Node:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self, node=None):
        self.root = node

    def add(self, item=None):
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
            return

        queue = []
        queue.append(self.root)
        while True:
            node = queue.pop(0)
            if node.lchild is None:
                node.lchild = new_node
                return
            elif node.rchild is None:
                node.rchild = new_node
                return
            else:
                queue.append(node.lchild)
                queue.append(node.rchild)

    # 广度优先遍历
    def breadth_travel(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.item)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    # 深度优先遍历, 前序遍历
    def preorder_travel(self, root):
        if self.root is None:
            return
        print(root.item, end=" ")
        if root.lchild is not None:
            self.preorder_travel(root.lchild)
        if root.rchild is not None:
            self.preorder_travel(root.rchild)

    # 深度优先遍历, 中序遍历
    def inorder_travel(self, root):
        if self.root is None:
            return
        if root.lchild is not None:
            self.inorder_travel(root.lchild)
        print(root.item, end=" ")
        if root.rchild is not None:
            self.inorder_travel(root.rchild)

    # 深度优先遍历, 后序遍历
    def postorder_travel(self, root):
        if root is None:
            return
        if root.lchild is not None:
            self.postorder_travel(root.lchild)
        if root.rchild is not None:
            self.postorder_travel(root.rchild)
        print(root.item, end=" ")

    #  层序遍历
    def levelorder_travel(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


# 3. 编写测试函数, 用于测试对应的功能.
# 3.1 定义函数 dm01_测试节点和二叉树()
def dm01_测试节点和二叉树():
    # 1. 创建节点
    node1 = Node('A')
    # 2. 打印节点的 元素域, 左子树, 右子树.
    print(node1.item)  # A
    print(node1.lchild)  # None
    print(node1.rchild)  # None
    print('-' * 23)
    # 3. 测试二叉树.
    # bt = BinaryTree()       # 空的
    # print(bt.root)          # None
    bt = BinaryTree(node1)
    print(bt.root)  # 根节点(的地址)
    print(bt.root.item)  # 根节点的元素域 -> A

# 3.2 定义函数 dm02_模拟队列取元素()
def dm02_模拟队列取元素():
    # 1. 创建队列, 特点: 先进先出
    queue = []
    # 2. 模拟往队列中添加元素.
    queue.append('A')
    queue.append('B')
    queue.append('C')
    # 3. 模拟从队列中取出元素.
    print(queue.pop(0))  # A 删除索引为0的元素, 并返回该元素, 即: 模拟从 队列中获取 元素.
    print(queue.pop(0))  # B
    print(queue.pop(0))  # C
    # 4.打印队列
    print(queue)  # ['A', 'B', 'C']

# 3.3 定义函数 dm03_广度优先遍历()
def dm03_广度优先遍历():
    # 1. 创建二叉树对象.
    bt = BinaryTree()
    # 2. 添加元素.
    bt.add('A')
    bt.add('B')
    bt.add('C')
    bt.add('D')
    bt.add('E')
    bt.add('F')
    bt.add('G')
    bt.add('H')
    bt.add('I')
    bt.add('J')
    # 3. 广度优先遍历.
    bt.breadth_travel()

# 3.4 定义函数 dm04_深度优先遍历()
def dm04_深度优先遍历():
    # 1.创建二叉树对象.
    bt = BinaryTree()
    # 2. 添加元素.
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    # 3. 深度优先遍历.
    print('先序(根左右): ', end=' ')
    bt.preorder_travel(bt.root)
    print('\n中序(左根右): ', end=' ')
    bt.inorder_travel(bt.root)
    print('\n后序(左右根): ', end=' ')
    bt.postorder_travel(bt.root)

if __name__ == '__main__':
    dm01_测试节点和二叉树()
    print('-' * 23)
    dm02_模拟队列取元素()
    print('-' * 23)
    dm03_广度优先遍历()
    print('-' * 23)
    dm04_深度优先遍历()
