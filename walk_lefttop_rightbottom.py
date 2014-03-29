__author__ = 'changyunglin'

def Question():
    '''You are given a 2-Dimensional array with M rows and N columns.
    You are initially positioned at (0,0) which is the top-left cell in the array.
    You are allowed to move either right or downwards. The array is filled with 1's and 0's.
    A 1 indicates that you can move through that cell, a 0 indicates that you cannot move
    through the cell. Given a function numberOfPaths which takes in the above 2-D array,
    return the number of paths from the top-left cell to the bottom-right cell
    (i.e. (0,0) to (M-1,N-1)).

    This is the same as 'sub-string' problem. The route is the sub-string for the current common string number
    '''

matrix = [[1,1,1,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,1,1]]

count = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for r in range(4):
    for c in range(4):
        if r == 0 and c == 0:       # initialize
            count[r][c] = 1
            pass
        if matrix[r][c] == 0:       # other cases where cell = 0
            count[r][c] = 0
        else:                       # other cases where cell = 1
            count[r][c] = 1         # assign count = 1
            if (r-1 >= 0) and (c-1 >= 0):   # give a boundary for row and col >= 0 (start from the left up corner)
                count[r][c] = count[r-1][c] + count[r][c-1] # check the top and left part, because it's where it can comes from.

for e in count:
    print(e)


'''
Q:
Find the shortest path in a maze (from origin to destination). I believe we are supposed to use Dijkstra or BFS.
'''
'''
A:
As far as I remember, mazes are generally solved using DFS. In this problem, there are 2 parts (i) find the
destination/exit in the maze (ii) find the shortest path from start to destination. If there is no other information
available about the maze, I think we can make 2 assumptions
(i) the number of edges in the path is its length
(ii) there is only one exit/destination in the maze.
Using the above assumption, a simple solution is: (i) find destination using DFS
(ii) apply Dijkstra's algorithm to find shortest path.
Total runtime = O((|V|+|E|)*log|V|) ... Dijkstra's runtime dominates DFS's runtime'''