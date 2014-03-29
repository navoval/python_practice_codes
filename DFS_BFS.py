__author__ = 'changyunglin'

# these two are similar. the big different is BFS use queue, and DFS use stack.
# For python, BFS append element at the end of the list (queue)
# DFS add the element at the begining of the list (stack)
# this two methods are iterative BFS and DFS
def bfs(start, target, GRAPH):
    'Use queue to search'
    print 'Source: %s Target: %s' % (start, target)
    queue = [start]
    visited = []

    while len(queue) > 0:
        x = queue.pop(0)
        if x == target:
            visited.append(x)
            return visited
        elif x not in visited:
            visited = visited + [x]
            # visited.append(x)
            if GRAPH[x] is not None:
                'add node at the end of the queue'
                queue = queue + GRAPH[x]    # append x's adjacency nodes in queue
    return visited

def dfs(start, target, GRAPH):
    'Use a STACK to search'
    print 'Source: %s Target: %s' % (start, target)
    stack = [start]
    visited = []

    while len(stack) > 0:
        x = stack.pop(0)
        if x == target:
            visited.append(x)
            return visited
        elif x not in visited:
            visited += [x]
            if GRAPH[x] is not None:
                'add node at the top of the stack'
                stack = GRAPH[x] + stack        # stack: left side of list is open end
    return visited

GRAPH = {1: [2,3], 2: [14,5], 3: [6], 14: None, 5: [7,8], 6: None, 7: None, 8: None}
print "BFS Path",bfs(1,7,GRAPH)
print "DFS Path",dfs(2,7,GRAPH)
print "="*80
print "BFS Path",bfs(1,3,GRAPH)
print "DFS Path",dfs(1,6,GRAPH)
