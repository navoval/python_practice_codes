__author__ = 'changyunglin'

# create a shuffle method
# assume we have perfect random generator
# Our idea is that iterate from 1 to 52 index, create a random number by using random generator as index
# and swap the number of index pointed to with the first element. Then mark the first as dead, swap with the next one
def Question():
    '''
    write a function to perfect shuffle a deck of cards
    in cracking code Chap-18.2
    '''
import random


def array_swap(array, a, b):
    tmp = array[b]
    array[b] = array[a]
    array[a] = tmp
    return array


def shuffle(array):
    if len(array) != card_number:
        print ('Should have 52 cards')
    else:
        for i in range(card_number):  # but range does not include number 10
            if len(array[i:]) > 2:
                random_index = random.randint(i, card_number-1)
                # Return a random integer N such that a <= N <= b (include b)
                array = array_swap(array, i, random_index)
            else:
                if len(array[i:]) == 2:
                    array = array_swap(array, i, i+1)
                else:
                    return array


card_number = 52
array = range(1, card_number + 1)  # range does not incclude the last one
print(len(array))
print(array)
print(shuffle(array))