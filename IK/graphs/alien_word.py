"""
The time complexity of the algorithm is:
1. creating graph
    O(n + alphabet_size), where n is total number of words in dictionary
    and alphabet_size is the number of alphabet_size
2. to, word2 = ogical sord complexity: O(V+E))
    And in our case it is O(n + alphabet_size)
"""
def create_graph(words):
    graph = {}
    words_len = len(words)

    #Find all the unique char in the dict
    unique_char = set()
    for w in words:
        unique_char = unique_char.union(set(w))

    # create graph with with vertex having all the unique char
    for ch in unique_char:
        graph[ord(ch) - ord('a')]=[]

    # Process all the adjacent words and add the edges if exits to the vertex
    for i in range(words_len - 1):
        # Take the two words and find the first mismatching char
        word1, word2 = words[i],words[i+1]
        for j in range(min(len(word1),len(word2))):
            # If found mismatch add and edge from char of word1 to word2
            if word1[j] != word2[j]:
                numeric_ch1 = ord(word1[j]) - ord('a')
                numeric_ch2 = ord(word2[j]) - ord('a')
                # Add the edges to the vertex in the graph
                graph[numeric_ch1].append(numeric_ch2)
                break
    return graph

def topological_sort_util(graph,visited,node,stack):
    visited[node] = True
    if node in graph:
        for v in graph[node]:
            if not visited[v]:
                topological_sort_util(graph,visited,v,stack)
        stack.append(node)

def topological_sort(graph):
    if len(graph) == 0:
        return

    # set all thge nodes as not visited
    visited = [False] * len(graph)
    stack = []

    # Check for all the nodes of the graph
    for node in graph.keys():
        if not visited[node]:
            topological_sort_util(graph,visited,node,stack)

    return stack

def find_order(word_dict):
    if len(word_dict) == 0:
        print("No word present in dictionary.")

    graph = create_graph(word_dict)
    ch_order = topological_sort(graph)

    while(len(ch_order) != 0):
        # convert it to char
        to_char = chr(ch_order.pop() + ord('a'))
        print(to_char, end= " ")

    print()

word_dict = ["baa", "abcd", "abca", "cab", "cad"]

find_order(word_dict)
