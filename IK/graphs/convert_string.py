"""
Given dictionary of words and two strings a and b.

Covert a to b by changing only one character at a time and makig sure that
all the intermediate words in the dictionary.
Example:
dictionary: {"cat", "bat","had","hat","bad"}
a = "bat"
b = "had"

Solution:
 "bat" ->  "bad" -> "had"

 Implementation:
 Create graph from the dictionary where each word is the node of the graph and there is undirected
 edge between two nodes if one word can be converted to next word by changing one character.

 After the creation of the grph do the BFS search for the given string "a".
"""
import collections
import string

dictionary = ["cat", "bat","had","hat","bad"]

def create_graph():
    graph = collections.defaultdict(list) # provides the deafult dict with empty []
    letters = string.ascii_lowercase # returns english alphabets

    for word in dictionary:
        for i in range(len(word)):
            # change 1 character and check if it's present in dictionary
            for char in letters:
                intermediate_word = word[:i]+char+word[i+1:]
                if intermediate_word in dictionary and intermediate_word != word:
                    graph[word].append(intermediate_word)

    return graph

def convert_string(graph, start,target):
    # Store the multiple paths from start to target
    paths = collections.deque([[start]])
    # Stores the already extended nodes so we don't traverse same node multiple time
    extended = set()

    # perform classical BFS
    while len(paths) != 0:
        current_path = paths.popleft()
        current_word = current_path[-1]
        if current_word == target:
            return current_path
        elif current_word in extended:
            # we already traverse this path
            continue

        # add the current_word to the extended
        extended.union(current_word)
        # Visit all the nodes accesible from current_word
        transform_word = graph[current_word]
        for word in transform_word:
            if word not in current_path:
                # this path need to be explore add
                paths.append(current_path[:] + [word])

    # no such transformation is found
    return []

graph = create_graph()
path = convert_string(graph, "bat", "had")
print("-> ".join(path))
