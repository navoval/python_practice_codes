__author__ = 'changyunglin'
# coding=UTF-8

'''

# from: http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
'''
class Node:

    def __init__(self, data):
        '''
        Node constructor
        @param data: node data object
        '''
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return "Node with Data: %d" % self.data

    def insert(self, data):
        '''
        Insert bew node with data
        @param data: node data object to insert
        '''
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        '''
        Lookup node containing data
        @param data: node data object to look up
        @param parent: node's parent
        @returns: node and node's parent if found or None
        '''
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)

        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        '''
        Return the number of children for a given node
        @return: number of children: 0,1,2
        '''
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def descendant_count(self):
        '''
        Counts all descendant nodes
        '''
        count = 0
        if self.left:
            count += 1 + self.left.descendant_count()
        if self.right:
            count += 1 + self.right.descendant_count()
        return count

    def delete(self, data):
        '''
        Delete node containing data
        @param data: node's content to delete
        '''
        node, parent = self.lookup(data)
        if node:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, then remove it
                # remove the reference to this node in the parent
                if parent.left is node:
                    parent.left = None
                if parent.right is node:
                    parent.right = None
                del node
            # if node have 1 child
            # simply promote the child to take the place of its parent
            elif children_count == 1:
                # make sure which child, left or right
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if parent:
                    # link the current node's parent to current node's child
                    if parent.left is node:
                        parent.left = child     # reassign the parent left to child (new one - node.left)
                    else:
                        parent.right = child
                del node
            # if node have 2 more children
            # What we need is a node that will preserve the binary search tree relationships for both of the
            # existing left and right subtrees. The node that will do this is the node that has the next-largest
            # key in the tree. We call this node the successor. Only need to search the right side of tree.
            # The minimum valued key in any binary search tree is the leftmost child of the tree
            else:
                parent = node
                successor = node.right      # next largest number should be on the right
                while successor.left:       # walk to the left, since the next largest should be on the left side of the right sub-tree
                    parent = successor
                    successor = successor.left
                # replace node by it's successor data
                node.data = successor.data
                # fix successor's parent's child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                # we walk to the last biggest node, and use the children count to do the delete.

    def print_tree(self):
        '''
        print inorder
        '''
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
        # tree traversal





root = Node(8)
l = [3, 10, 1, 6, 4, 7, 14, 13, 21]
[root.insert(e) for e in l]

root.print_tree()
print

root.delete(10)
root.print_tree()
#
# root.delete(3)
# root.print_tree()
#
# root.delete(3)
# # root.print_tree()
# print('Look up:', root.lookup(21))
