__author__ = 'changyunglin'
# find out the missing value in a sorted list

l = [0,1,2,3,6,7,10,20]
length = len(l)
missing_number_list = []

for i in xrange(len(l)):
    if i == 0:
        pass
    elif l[i]-1 == l[i-1]:
        pass
    else:
        miss_value_count = l[i] - l[i-1] - 1
        for _ in range(miss_value_count):
            miss_value = l[i-1] + 1
            print 'missing value: ', miss_value
    print 'exist value: ', l[i]




