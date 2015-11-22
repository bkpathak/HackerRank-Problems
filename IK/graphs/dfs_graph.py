def dfs_util(node, visited,graph):
    print(node,end = " ")
    visited[node] = True

    # recurse through all the adjacent nodes
    for v in graph[node]:
        if not visited[v]:
            dfs_util(v,visited,graph)

def dfs_traverse(graph):
    if len(graph) == 0:
        return

    visited = [False] * len(graph)

    # check every node of the graph
    for node in graph.keys():
        if not visited[node]:
            dfs_util(node,visited,graph)
    print()


graph = {0:[1,2],1:[2],2:[0,3],3:[3]}

dfs_traverse(graph)
