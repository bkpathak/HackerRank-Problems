from collections import deque
def bfs_traverse(graph,start_node):
    if len(graph) == 0:
        return

    # Set all the node is not visited
    visited = [False] * len(graph)
    queue = deque()

    # Aadd the starting node to the graph
    queue.append(start_node)
    visited[start_node] = True
    while len(queue) > 0:
        current_node = queue.popleft()
        print(current_node,end = " ")

        for v in graph[current_node]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    print()

graph = {0:[1,2],1:[2],2:[0,3],3:[3]}

bfs_traverse(graph,2)
