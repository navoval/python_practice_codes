__author__ = 'changyunglin'
'''
Question:
1. find all the combinations of a string in lowercase and uppercase. 
For example, string "ab" -> "ab", "Ab", "aB", "AB". 
So, you will have 2^n (n = number of chars in the string) output strings. 
The goal is for you to test each of these string and see if it match a hidden string.
'''
def toDigit(l):
    return [int(char) for char in str(l)]

def chang2UppLower(original, digit):
    result = ''
    o = list(original)
    for i in range(len(digit)):
        if int(digit[i]) == 0:
            result += o[i].lower()
        elif int(digit[i]) == 1:
            result += o[i].upper()
        else:
            print('Error')
    return result


s = 'abc'
l = [['1', '0', '0'], ['0', '1', '1'], ['1', '1', '1']]

l1 = ['100', '011', '111', '010']   # if only 011, python will read as 'octal' numeral system which is 9 not 011
for e in l1:
    t = toDigit(e)
    print(chang2UppLower(s, t))

'''
Store a set of sudden-death tournament results in a compact format (eg. a bit array) 
and a set of predicted match results (also in a bit array). Score the predictions, 
giving one point per correctly guessed match, without unpacking the bit array into 
a more convenient format (ie. you have to traverse the tree in-place).

# not sure if this is the right answer

'''
# use the previous code, compare the 2 element if equal

string1 = 'abeHeW'
score = ['100101', '111011']
predict = ['100100', '111011']

s1 = []
p1 = []
[s1.append(toDigit(e)) for e in score]
[p1.append(toDigit(e)) for e in predict]
print s1
print p1


for index, value in enumerate(s1):
    for i, v in enumerate(value):
        if v == p1[index][i]:
            print "s1 = p1 in idx: s1: %s, p1: %s" % (i, i)
        else:
            print "s1 != p1 in idx: %s, %s. s1: %s p1: %s" % (index, i, s1[index][i], p1[index][i])


