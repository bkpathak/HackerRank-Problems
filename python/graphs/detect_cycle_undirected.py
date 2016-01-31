"""
We are representing the Graph as dictionary. The key of the dictionary
is the node of the graph and the value is the list which contains all
the connected nodes.

The algorithm for deteccting cycle in undirected graph is:
Let us assume the graph has no cycle, i.e. it is a tree. And if we
look at a tree, each edge from a node:
1.either reaches to its one and only parent, which is one level
above it.
2.or reaches to its children, which are one level below it.
So if a node has any other edge which is not among the two described
above, it will obviously connect the node to one of its ancestors
other than its parent. This will form a CYCLE.

"""
graph = {}

def detect_cycle():
    if len(graph) == 0:
        return False

    visited = [False] * len(graph)
    # Recurse through all the nodes
    for node in graph.keys():
        if not visited[node]:
            if is_cycle(node, visited, -1):
                return True
    return False

def is_cycle(node,visited,parent):
    visited[node] = True

    # Call the is_cycle recursively on all the vertex accessible
    # from the current node.
    for v in graph[node]:
        # Only recurse if the adjacent node is not visited
        if not visited[v]:
            if is_cycle(v,visited,node):
                return True
        # If v is visited and not the parent of the current node,
        # then it is visited.
        elif v != parent:
            return True

    return False

graph = {0:[1,2],1:[0,2],2:[1,0],3:[0,4],4:[3]}

if detect_cycle():
    print("CYCLE present.")
else:
    print("NO CYCLE.")
