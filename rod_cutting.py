__author__ = 'changyunglin'

def Question():
    '''
    This is rod cutting question: find the maximum revenue rj and optimal size sj of the first piece to cut off for each rod size j.
    http://www.adchilds.com/2012/04/11/cut-rod-dynamic-programming/
    '''

def rod_cutting(n, price, c):
    revenue = [0] * (n+1)
    size = [0] * (n+1)
    for j in range(1, n+1):
        q = price[j]   # this take cares of no cut
        for i in range(1, j+1):
            rev = price[i] + revenue[j - i] - c
            if q < rev:
                q = rev
                size[j] = i
            # else:
            #     size[j] = i


        revenue[j] = q

    print 'revenue: ', revenue
    print 'size: ', size


price = [0,1,5,8,9,10,17,17,20,24,30]
print 'length: ', (0,1,2,3,4,5,6,7,8,9,10)
print 'price: ', price
rod_cutting(n=len(price)-1, price=price, c=1)




