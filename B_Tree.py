__author__ = 'changyunglin'
# coding=UTF-8


class Node:
    def __init__(self, info):

        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class serachTree:

    def __init__(self):
        self.root = None

    # create a binary search trre
    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            s = self.root
            while 1:
                if val < current.info:      # 往左
                    if current.left:        # 左邊是否有點
                        current = current.left  # 左邊有點
                    else:
                        current.left = Node(val)    # 沒點，創建新點
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    # tree traversal
    def bft(self):
        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
                out.append("\n")
            out.append(str(current_node.info) + " ")
            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
        print(''.join(out))

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.info)
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.info)
            self.preorder(node.right)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.preorder(node.right)
            self.preorder(node.right)
            print(node.info)


tree = serachTree()
arr = [8,3,1,6,4,7,10,14,13]
print('original order: ', arr)
for i in arr:
    tree.create(i)
print 'Breadth-First Traversal'
tree.bft()
print 'Inorder Traversal'
tree.inorder(tree.root)
# print 'Preorder Traversal'
# tree.preorder(tree.root)
# print 'Postorder Traversal'
# tree.postorder(tree.root)