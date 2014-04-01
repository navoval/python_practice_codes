__author__ = 'changyunglin'
# coding=UTF-8
import itertools


def Question():

    question = '''
    You have n - 1 numbers from 1 to n. Your task is to find the missing number.
    I.e.
    n = 5
    v = [4, 2, 5, 1]
    The result is 3.
    '''
    solution_idea = ''' Add all the numbers in the array as r1. Calculate the sum of n numbers using n*(n+1)/2 = r2
    substract r1 from r2. You will get the lost number'''

def Answer1():
    def find_missing_value(l, n):
        '''
        Find a missing value in a serial numbers
        This method can not include number 0 in the list
        '''
        r1 = sum(l)
        r2 = n*(n+1)/2
        missing_value = r2 - r1
        return missing_value

    N = 10
    L = [1,2,3,4,5,6,7,8,10]    # missing 8
    print find_missing_value(l=L, n=N)

def Question2():
    question2 = '''
    Given an array with numbers, your task is to find 4 numbers that will satisfy this equation:
    A + B + C = D
    '''

    answer2 = ''' This is 4-SUM problem. We convert A+B+C=D to A+B=D-C, calculate all the A+B,D-C need two double loops.
    we can calculate A+B and hash it, remember to record A,B position (idx) in array.
     -- to make sure no number is used more than once it will better to store indices instead of the actual numbers for each sum --

    The complexity, in general, will be O(n) * O(nlogn) O(n^2logn)
    '''

def Answer2():

    def left_part(L):
        d = {}
        for subset in itertools.combinations(L, 2):
            # it uses idx to record the position
            V = subset[0]+subset[1]
            if V in d.keys():
                d[V].append(subset)
            else:
                d[V] = [subset]
        return d

    def right_part(L):
        d = {}
        for subset in itertools.combinations(L, 2):
            V = subset[1] - subset[0]
            if V in d.keys():
                d[V].append(subset)
            else:
                d[V] = [subset]
        return d

    def check_equal(d1, d2):
        for k in d1.keys():
            if k in d2.keys():
                t1 = d1[k]      # list of tuples
                t2 = d2[k]
                for e1 in t1:
                    for e2 in t2:
                        if e1 != e2:
                            if e1[0] != e2[0] and e1[0] != e2[0]:
                                if e1[1] != t2[0] and e1[1] != e2[0]:
                                    return e1, e2

    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    hash1 = left_part(L)       # A+B
    hash2 = right_part(L)       # D-C
    print('+', hash1)
    print('-', hash2)
    result = check_equal(d1=hash1, d2=hash2)
    print result

def Question3():
    question = '''
    How many squares are present in an NxN grid?
    In an MxN grid, how many squares are present and how many rectangles?
    '''

    solution_idea = '''
    1. squares in NxN grid
        1X1	 ->  (N)^2
        2X2	 ->  (N-1)^2
        3X3  ->  (N-2)^2
        ...
        NxN  ->  (1)^2
        So, total no. of squares=sigma(N^2) over N
                        =(N)*(N+1)*(2*N+1)/6

    2.squares in MxN grid
        let M>N //swap if M<N
        let k=M-N
        1x1  ->  (N+k)x(N)
        2x2  ->  (N-1+k)x(N-1)
        3X3  -> (N-2+k)x(N-2)
        ...
        NxN  ->(1+k)x(1)
        So, total no. of squares = sigma((N+k)*(N)) over N
                                =sigma(N^2 + k*N)
                                =sigma(N^2) +k*sigma(N)
                                =(N)(N+1)(2*N+1)/6 + k*N*(N+1)/2
                                ** deduction from here: http://nubnub.blog.163.com/blog/static/169186347201182795656783/ **
    3.rectangles in MxN grid
        In an MxN grid you have M+1 horizontal lines
        and N+1 vertical lines to enclose a rectangle.
        If we choose 2 out of M+1 lines and 2 out of N+1 lines then the intersection of these 4 lines makes a rectangle.

        so,answer is 	  (N+1)C(2) * ((M+1)C(2))   		// choose r from n
			                =(N*(N+1)/(2)) * (M*(M+1)/2)
    '''
    '''使用取邊界的概念來解決 rectangles 的問題 與 square的問題解法不相同'''

def Answer3():
    import scipy.misc as sm

    def rectangles_numbers(M, N):
        '''
        正方形是屬於長方形的一種。或者說，正方形是長方形的特例。矩形的定義是四個角皆為 90° 的四邊形。
        如果要算不包含正方形的長方形，只需把所有的算出，然後減去正方形的個數。
        '''
        horizontal = sm.comb(M+1, 2, exact=True)
        vertical = sm.comb(N+1, 2, exact=True)
        return horizontal * vertical

    def square_inMxN(M, N):

        if M > N:
            k = M - N
            return N*(N+1)*(2*N+1)/6 + k*N*(N+1)/2
        else:
            k = N - M
            return M*(M+1)*(2*M+1)/6 + k*M*(M+1)/2

    N = 3
    M = 2
    print 'rec', rectangles_numbers(M=M, N=N)
    print 'squ', square_inMxN(M=M, N=N)

def Question4():
    question = '''you have an array which has a set of positive and negative numbers,
    print all the subset sum which is equal to 0.
    eg:  2, 1, -1, 0, 2, -1, -1
    o/p:    1, -1
            1, -1, 0
            0
            2, -1, -1
    '''
    solution_idea = '''
    This is similar to 4SUM question. Instead of 4 number add up to 0 ( A+B+C+D=0 ), you have many numbers add up to 0.
    You use the 4SUM problem method, and go through every possible solution from 1-SUM + 2-SUM + 3-SUM + ...
    '''

def Answer4():
    '''
    Instead of doing to hash table, we do one hash table and set target as ZERO. Finding the negative value in the keys. eg: key = 1,
    we find key: -1
    '''

    def makeHashTable(L):
        '''
        This method will return all the possible values in this list. Since we wants zero, simply access the ZERO key in dictionary.
        Also, because we use index to access the number in the array,
        there could have duplicate values which makes zero (but they are from different idx).
        We need another function to clean duplicate values.
        Since we calculate all the possible values provided by an array, we can easily find value we want, but the complexity is high.
        It's O(n) * O(n^2log(n))
        Same idea as Question 2, but more expensive and more flexibility.
        '''
        d = {}
        for r in range(len(L)):     # O(n)
            for subset in itertools.combinations(L, r+1):   # O(n) * O(nlogn) O(n^2logn)
                V = sum(subset)
                # can add code here to decide if we only want to store the ZERO value to save memory
                if V in d.keys():
                    d[V].append(subset)
                else:
                    d[V] = [subset]
        return d

    L = [2, 1, -1, 0, 2, -1, -1]
    print(makeHashTable(L).keys())
    print(makeHashTable(L)[0])


# Answer1()
# Answer2()
# Answer3()
# Answer4()
