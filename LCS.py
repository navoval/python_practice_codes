__author__ = 'changyunglin'

# def longest_common_substring(s1, s2):
#     m = [[0] * (1 + len(s2)) for _ in xrange(1 + len(s1))]  # build up a matrix
#     longest, x_longest_index = 0, 0
#     for x in xrange(1, 1 + len(s1)):
#         for y in xrange(1, 1 + len(s2)):
#             if s1[x - 1] == s2[y - 1]:
#                 m[x][y] = m[x - 1][y - 1] + 1
#                 if m[x][y] > longest:   # becasue this matrix is not continuous save lingest number,
#                                         # so needs consider the case that the longest string break, like our case
#                     longest = m[x][y]
#                     x_longest_index = x
#             else:
#                 m[x][y] = 0
#     print('x_longest', x_longest_index)
#     print('longest', longest)
#     return s1[x_longest_index - longest: x_longest_index], m        # use index to get the string


def longest_common_substring(s1, s2):
    m = [[0] * (len(s2)) for _ in xrange(len(s1))]  # build up a matrix
    maxsofar, x_longest_index = 0, 0
    for x in xrange(len(s1)):
        for y in xrange(len(s2)): 
            if s1[x] == s2[y]:
                if x == 0 or y == 0:    # first row and first column
                    m[x][y] = 1
                else:   # other cases
                    m[x][y] = m[x - 1][y - 1] + 1
                    if m[x][y] > maxsofar:   # becasue this matrix is not continuous save lingest number,
                                            # so needs consider the case that the longest string break, like our case
                        maxsofar = m[x][y]
                        x_longest_index = x     # index to remember where is the longest index right now.
            else:
                m[x][y] = 0
    print('x_longest', x_longest_index)
    print('maxsofar', maxsofar)
    return s1[x_longest_index - maxsofar+1: x_longest_index+1], m        # use index to get the string



# the good thing about this method is once the matrix is not the same, it save to 0 instead of saving the longest
# once there are multiply sub-string, you can use the matrix to trace back where are those sub-string

S1 = 'photograph'
S2 = 'tomography'
string, m = longest_common_substring(s1=S1, s2=S2)
print(string)
print 'the size of the matrix should be {0} x {1}', len(S1), len(S2)
for e in m:
    print(e)

S1 = 'cabccb'
S2 = 'babcba'
string, m = longest_common_substring(s1=S1, s2=S2)
print(string)
print 'the size of the matrix should be {0} x {1}', len(S1), len(S2)
for e in m:
    print(e)
