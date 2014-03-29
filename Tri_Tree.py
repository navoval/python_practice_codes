__author__ = 'changyunglin'

# Question 2: Implement insert and delete in a tri-nary tree.
# finished build up Tri-Tree
# finished basic print Tri-Tree
# finished delete node function
# finished pretty print Tri-Tree

import pprint

class Node:

    def __init__(self, data=None):
        self.root = None
        self.left = None
        self.right = None
        self.center = None
        self.data = data
        self.level = None

    def insert(self, data):
        '''
        Insert element in Tri-Tree struct
        '''
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while 1:
                # left child
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                # center child
                elif data == current.data:
                    if current.center is None:
                        current.center = Node(data)
                        break
                    else:
                        current = current.center
                # right child
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
                else:
                    break

    def lookUp(self, value, parent=None):
        '''
        find look up data
        return node and node's parent if found or None
        '''
        # look in the left tree
        if value < self.data:
            if self.left is None:
                return None, None
            else:
                return self.left.lookUp(value, self)
        # look in the right tree
        elif value > self.data:
            if self.right is None:
                return None, None
            else:
                return self.right.lookUp(value, self)
        else:
            # find it
            # this ccould also means, there is another center node.
            if self.center is not None:
                return self.center.lookUp(value, self)
            return self, parent

    def childrenCount(self):
        '''
        Count how many children a node have
        '''

        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        if self.center:
            count += 1
        return count

    def deleteNode(self, node, parent):
        '''
        Consider three case by the number of children
        '''
        if node:
            children_count = node.childrenCount()
            if children_count == 0:  # it's leaf
                if parent.left is node:
                    parent.left = None
                if parent.right is node:
                    parent.right = None
                if parent.center is node: # parent.center is node
                    parent.center = None
                del node

            if children_count == 1:
                # decide which is the child
                if node.left:
                    child = node.left
                if node.right:
                    child = node.right
                if node.center:
                    child = node.center
                # link the current node's parent to current node's child
                if parent:
                    if parent.left is node:
                        parent.left = child
                    if parent.right is node:
                        parent.right = child
                    if parent.center is node:
                        parent.center = child
                del node

            if children_count == 2:
                if node.center is None:     # left and right like binary search tree
                    parent = node
                    successor = node.right
                    while successor.left:
                        parent = successor
                        successor = successor.left
                    # replace node by it's successor data
                    node.data = successor.data
                    # fix successor's parent's child
                    if parent.left == successor:
                        parent.left = successor.right
                    else:
                        parent.right = successor.right

                else:   # center is not none
                    # either 'center and left' or 'center and right'
                    # however, because the data in the center node is the same
                    # we can simply delete the center node without changing the balance
                    if node.left is None:   # center and right
                        del node.center
                    else:   # node.right is None
                        del node.center

            if children_count == 3:
            # replace the delete node with center node
                del node.center

    def inorder(self, node):
        '''
        Inorder print
        '''
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.center)
            self.inorder(node.right)

    def delete(self, value):
        '''
        Delete target node
        '''
        node, parent = self.lookUp(value)
        self.deleteNode(node, parent)

    def printStructure(self):
        '''
        Build Tree shape structure
        '''
        self.root.level = 0
        queue = [self.root]
        current_level = self.root.level + 1
        levelDict = {}
        levelDict[self.root.level] = [str(self.root.data)]

        while len(queue) > 0:
            next_level = []
            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                next_level.append(str(current_node.left.data))
            else:
                next_level.append(" ")

            if current_node.center:
                current_node.center.level = current_level + 1
                queue.append(current_node.center)
                next_level.append(str(current_node.center.data))
            else:
                next_level.append(" ")

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                next_level.append(str(current_node.right.data))
            else:
                next_level.append(" ")

            if levelDict.has_key(current_level):
                levelDict[current_level].extend(next_level)
            else:
                levelDict[current_level] = next_level
        print 'Node in each level'
        pprint.pprint(levelDict)
        return levelDict

    def prettyPrint(self):
        '''
        Pretty print Tree Structure
        '''
        structureDict = self.printStructure()
        levels = len(structureDict.keys())
        grid = 3**(levels-1)
        space_list = []
        for k in structureDict:
            space = ((grid/3**int(k)))/2    # space for left and right
            space_list.append(space)
        print "="*40 + ' Tree shap ' + "="*40
        for k in structureDict.keys():
            S = ''
            for v in structureDict[k]:
                S += (space_list[k]*' '+ v + space_list[k]*' ')
            print S


l1 = [5, 4, 9, 5, 7, 2, 2]
tree1 = Node()

[tree1.insert(e) for e in l1]

# Test Cases
print "Test Case 1"
print "Original Tree"
print "="*80
print "Tree element inorder"
print tree1.inorder(tree1.root)
print "="*40 + " Tree Structure " + "="*40
print tree1.prettyPrint()

# tree1.print_tree()

print "="*80
print'Delete node 7 in tree'
tree1.root.delete(7)
print "Tree element inorder"
print tree1.inorder(tree1.root)
print "="*40 + " Tree Structure " + "="*40
print tree1.prettyPrint()

print "="*80
print'Delete node 5 in tree'
tree1.root.delete(5)
print "Tree element inorder"
print tree1.inorder(tree1.root)
print "="*40 + " Tree Structure " + "="*40
print tree1.prettyPrint()


print
print
print "Test Case 2: Add more elements: 9 , 10"
l2 = [5, 4, 9, 5, 7, 2, 2, 9, 10]
tree2 = Node()

[tree2.insert(e) for e in l2]

# Test Cases
print "Original Tree"
print "="*80
print "Tree element inorder"
print tree2.inorder(tree2.root)
print "="*40 + " Tree Structure " + "="*40
print tree2.prettyPrint()

print "="*80
print'Delete node 7 in tree'
tree2.root.delete(7)
print "Tree element inorder"
print tree2.inorder(tree2.root)
print "="*40 + " Tree Structure " + "="*40
print tree2.prettyPrint()

print "="*80
print'Delete node 9 in tree'
tree2.root.delete(9)
print "Tree element inorder"
print tree2.inorder(tree2.root)
print "="*40 + " Tree Structure " + "="*40
print tree2.prettyPrint()

