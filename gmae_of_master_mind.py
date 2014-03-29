__author__ = 'changyunglin'

# We treat lower and Upper case differently.

def find(string, target):
    '''
    Return multi index if the element appear multiple times
    '''
    # for i, char in enumerate(string):
    #     if char == target:
    #         yield i
    # this is same as below, the different is, yield return result each round.
    # use list comprehension give a whole list of results
    return [i for i, char in enumerate(string) if char == target]


def check(ans, guess):
    '''
    Use dictionary to store frequency. It is easier than use list and compare with index
    dict : {a: [1]} it stores the index in the list
    '''
    d = {}
    hit_count = 0
    pseudo_count = 0
    false_count = 0

    # put the ans into a dictionary
    for e in ans:
        d[e] = find(string=ans, target=e)
    for idx, e in enumerate(guess):
        if e in d.keys():
            if idx in d[e]:
                hit_count += 1
            else:
                pseudo_count += 1
        else:
            false_count += 1
    # print(d)
    return hit_count, pseudo_count, false_count
my_mind = 'YBRR'
print(my_mind)
guess = raw_input("Enter RGBY to guess my mind (Use capital)")
hit, pseudo, false = check(ans=my_mind, guess=guess)
print(hit)
print(pseudo)
print(false)




