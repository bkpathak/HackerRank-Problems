"""
The idea on the directed Graph is to keep the track of node which is not visited
completely.

The used of stack is to keep the track of the node which is still needs to be explored
fully.If we reach the node in stack that means we reach the node that is not completely
visited, whcih implies that there is a cycle.
"""

def is_cycle(node,stack, visited):
    # Mark the current node visited and part of the stack
    stack[node] = True
    visited[node] = True

    for v in graph[node]:
        if not visited[v] and is_cycle(v, stack, visited):
            return True
        # If it's part of stack then we reach the node
        elif stack[v]:
            return True

    # Vertex is completely visited, remove it from stack
    stack[v] = False
    return False

def detect_cycle():
    if len(graph) == 0:
        return False

    # Set all the vertex as not visited
    visited = [False] * len(graph)
    stack = [False] * len(graph)

    # Recurse through all the nodes in graph
    for node in graph.keys():
        if is_cycle(node,stack,visited):
            return True
    return False

graph = {0:[1,2],1:[2],2:[0,3],3:[3]}

if detect_cycle():
    print("CYCLE in graph.")
else:
    print("Graph doesn't have cycle.")
