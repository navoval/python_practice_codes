__author__ = 'changyunglin'
# graph is a dict structure
# find path in a graph by using dfs, lookup the adjance node in a dict structure


def bfs(graph, start, end):
    todo = [[start, [start]]]
    while len(todo) > 0:
        # pop out the node where we already checked
        (node, path) = todo.pop(0)
        # do bfs,
        for next_node in graph[node]:
            # instead of liking dfs, keep giving a new subnode
            # it still on the current node, and check it's adjacent node
            if next_node in path:
                continue
            elif next_node == end:
                yield path + [next_node]
            else:
                todo.append([next_node, path + [next_node]])


def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        # where do dfs, recursive call itself by giving a 'new' subnode. So it's dfs
        newpaths = find_all_path(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths
    '''
    return [find_all_path(graph, node, end, path) for node in graph[start]]
    '''


def find_a_path(graph, start, end, path=[]):
    # graph is a dict structure
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):    # if graph do not have this key
        return []
    paths = []
    for node in graph[start]:   # node is the value under key: start
        newpath = find_a_path(graph, node, end, path)   # dp call to find the node
        # code is the same as finding all nodes
        # once we find one, we return this one
        if newpath:
            return newpath
    return None

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

for path in find_a_path(graph, 'A', 'D'):
    print path

for path in find_all_path(graph, 'A', 'D'):
    print path

for path in bfs(graph, 'A', 'D'):
    print ':', path