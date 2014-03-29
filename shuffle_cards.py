__author__ = 'changyunglin'
import random

def Question():
    '''
    write a function to shuffle a deck of cards
    in cracking code Chap-18.2
    '''
def swap(A, B, L):
    L[A], L[B] = L[B], L[A]
    return L

l = [1,2,3,4,5,6,7,8,9,10]

print('before shuffle: ', l)

for i in range(len(l)):
    k = random.randint(0, len(l)-1)
    swap(i, k, l)
    print('after shuffle: ', l)

l1 = [1,2,3]
# print swap(l1[0], l1[2])