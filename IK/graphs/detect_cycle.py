"""
We are representing the Graph as dictionary. The key of the dictionary
is the node of the graph and the value is the list which contains all
the connected nodes.
"""

def detect_cycle(graph):
    if len(detect_cycle) == 1:
        return False

    visited = [False] * len(graph)

    for node in graph:
        if not visited[node]:

        if is_cycle(visited,graph):
            return True
    return False

def is_cycle(visited,graph):
