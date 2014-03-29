__author__ = 'changyunglin'

# implement knapsack problem

import numpy as np

W = 15  # W is maximum wight
n = 9   # n is the number of items
c = np.zeros(shape=(n+1, W+1))   # c is a nump matrix
WL = [0,3,5,7,4,3,9,2,11,5]   # a list of weights
VL = [0,2,3,3,4,4,5,7,8,8]    # a list of values
# we put a 0 at the begining of the WL and VL for index purpose

# note becasue the np marix start index at 0 NOT 1, so when you file in the value, take care about the index

def knapsack(c, n, W):
    for i in range(n+1):    # row
        c[i, 0] = 0
        for j in range(W+1):    # column
            if WL[i] <= j:
                new_value = VL[i] + c[i-1, (j-WL[i])]
                if new_value > c[i-1, j]:
                    c[i, j] = new_value
                else:
                    c[i, j] = c[i-1, j]
            else:
                c[i, j] = c[i-1, j]

    for row in c:
        print row

knapsack(c=c, n=n, W=W)

