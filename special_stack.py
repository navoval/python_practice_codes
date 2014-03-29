__author__ = 'changyunglin'


# Design a stack, which in addition to push and pop, also has a function to
# return the minimum element.



class Stack():

    def __init__(self):
        '''
        it have another list min = []
        stores the current min value for a stack, it's the same size as Stack (waste mem in big data)
        Ex: S =[2,4,1,] min = [2,2,1]
        '''
        self.items = []
        self.min = []
        self.current_min = 10000        # this can be achieve by assigning a really big number, but it's not that good
        # or you can have modify the pushupdate function by considering the initial stage

    def push(self, item):
        self.items.append(item)
        self.updatemin(item)

    def pop(self):
        tmp = self.items[-1]
        del self.items[-1]
        del self.min[-1]
        return tmp

    def updatemin(self, item):
        '''
        use another list to store current smallest number
        but this method is not good for big data set, it waste a lot of space
        '''
        if item < self.current_min:
            self.current_min = item
            self.min.append(item)
        else:
            self.min.append(self.current_min)

    def getmin(self):
        return self.min[-1]



s = Stack()

L = [1,2,-3,4,1,5,6,7]
for e in L:
    s.push(e)
print 's have: ', s.items
print 'pop s: ', s.pop()
print 'all items: ', s.items
print 'current min: ', s.getmin()
print 'min list', s.min






class Stack_big():
    '''
    for big data, instead of saving every stage of stack's minimum value
    we only store current minimum value and idx in a minimum_list to save space
    '''

    def __init__(self):
        self.items = []
        self.minimum_list = []
        self.current_min = None

    def push(self, item):
        self.items.append(item)
        self.pushUpdateMin(item)

    def pop(self):
        tmp = self.items[-1]
        self.popUpdateMin(tmp)
        del self.items[-1]
        return tmp

    def pushUpdateMin(self, item):
        # initial case
        if self.minimum_list == []:
            self.minimum_list.append((item, self.items.index(item)))
            self.current_min = item
        # other cases
        # store the current minimum index in a list, if it doesn't change, it wouldn't update
        elif item < self.current_min:
            self.minimum_list.append((item, self.items.index(item)))
            self.current_min = item

    def popUpdateMin(self, item):
        if self.items.index(item) == self.minimum_list[-1][1]:
            del self.minimum_list[-1]

s = Stack_big()
l = [1,2,3,45,6,0,98,10]
for e in l:
    s.push(e)
print 'specaill case'
print s.items
print s.minimum_list
print s.pop()
print s.pop()
print s.pop()
print s.minimum_list
print s.push(78)
print s.push(98)
print s.push(-78)
print s.minimum_list
print s.pop()
print s.minimum_list