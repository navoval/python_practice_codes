__author__ = 'changyunglin'

# Question: Take input  ex: 1234567 as string, and use function to change it to long
# Answer: We take input and put in list, and use index to access the each char. 
#         Since we change it into decimal, we have the previous * 10 to move digit, and add a new number in it.


def stringToLong(string):
    l = [string]
    previous = 0
    for i in range(len(l[0])):
        new = int(l[0][i])
        previous =  previous * 10 + new
    return previous


# test section

# use self build function
string = '123456789104124323'
print "original string: ", string
print "original string type: ", type(string)

s = stringToLong(string=string)

print 'value of string:', s
print 'type of string:', type(s)

# use buildin function

print "Use build in function to change string char into decimal ", long(string, 10)

