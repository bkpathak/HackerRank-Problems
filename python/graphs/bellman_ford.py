# Bellman Ford implementation
# Complexity : O(VE) using adjacency list

INT_MAX = 2 ** (32) - 1
def bellman_ford_shortest_path(graph, source_vertex):
    # Create the distance array and parent array
    distance = [INT_MAX] * len(graph)
    parent = [-1] * len(graph)

    # set the distance of source vertex from itself as 0
    distance[source_vertex] = 0

    # Loop through all the vertices -1 since max number of vertices
    # between two vertex cannot be more than (V-1)
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    parent[v] = u

    display(distance, parent)

def display(distance, parent):
    print("node   distance    parent")
    for i,j in enumerate(distance):
         print("{0}\t{1}\t\t{2}".format(i,j,parent[i]))


if __name__ == "__main__":
    graph = {
    0 : {1:4, 3:6, 2:5},
    1 : {2: -3},
    2 : {5:4},
    3 : {4: 2},
    4 : {5:2},
    5 : {4:1}
    }

    bellman_ford_shortest_path(graph,0)
