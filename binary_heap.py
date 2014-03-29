__author__ = 'changyunglin'
# coding=UTF-8


# the code is not working when, it need perculate up function

class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def swap(self, A, B):
        A, B = B, A

    def percUp(self, i):
        # compare current with it's parent, swap if it is smaller -> minHeap structure
        while i // 2 > 0:    # dividing the current node index by 2
            if self.heapList[i] < self.heapList[i // 2]:    # value of current node is less than the value of parent node
                # swap
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2  # get 商

    def insert(self, k):
        '''
        insert a new element: the idea is to append the element at the end of the list,
        and use percUp to swap the element to a proper position
        '''
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)


    def minChild(self, i):                                  # find the min child under current node.
                                                            # 只在乎父和子的大小關係，不在乎子之間的大小關係。回傳當前node的子的最小值
        if i * 2 + 1 > self.currentSize:                    # if right > total list length
            return i * 2                                    # then current smallest in left children
        else:                                               # have right children
            if self.heapList[i*2] < self.heapList[i*2+1]:   # compare the children
                return i * 2                                # if left is smaller than right
            else:
                return i * 2 + 1                            # if right is smaller than left

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            # get the smallest child under current node
            mc = self.minChild(i)
            # swap
            if self.heapList[i] > self.heapList[mc]:
                self.swap(self.heapList[i], self.heapList[mc])
                # tmp = self.heapList[i]
                # self.heapList[i] = self.heapList[mc]
                # self.heapList[mc] = tmp
            i = mc

    def delMin(self):
        '''
        delete an element: First, we will restore the root item by taking the last item in the list and moving it to the root position.
        Moving the last item maintains our heap structure property.
        However, we have probably destroyed the heap order property of our binary heap.
        Second, we will restore the heap order property (percDown) by pushing the new root node down the tree to its proper position.
        '''
        retval = self.heapList[1]                               # root
        self.heapList[1] = self.heapList[self.currentSize]      # copy the last element in the root
        self.currentSize -= 1                                   # redefine the size of the list
        self.heapList.pop()                                     # delete the last element in the list
        self.percDown(1)                                        # maintain the heap order, swap it down
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2         # why is // 2  ??
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
print(bh.heapList)

[bh.insert(e) for e in [1,2,3]]
# the result is wrong because it need up perup function
print(bh.heapList)
# bh.buildHeap(bh.heapList)
# print(bh.heapList)



