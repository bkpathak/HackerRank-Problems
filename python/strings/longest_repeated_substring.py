# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/suffixtrees.pdf
# This is the implementaion of suffix tree.
# https://en.wikipedia.org/wiki/Suffix_tree

# Main idea:
# Every substring of s is a prefix of some suffix of s.

# Application of Suffix Trie
# For a suffix Trie T and querry string q
# 1. Check whether q is substring of T
#    Follow the path for q starting from the root.
#    If you exhaust the query string, then q is in T
# 2. Check whether q is suffix of T
#    Follow the path for q starting from the root.
#    If you end at a leaf at the end of q, then q is a suffix of T
# 3. Count # of occurences of q in T
#    Follow the path for q starting from the root.
#    The number of leaves under the node you end up in is the
#    number of occurrences of q
# 4. Find the longest repeat in T
#    Find the deepest node that has at least 2 leaves under it.
# 5. Find the lexicographically
#    Start at the root, and follow the edge labeled with the
#    lexicographically (alphabetically) smallest letter

# Suffix Links
# Connects node epresenting “xα” to a node representing “α”

class SuffixNode(object):
    def __init__(self, suffix_link = None):
        self.children = {}
        if suffix_link is not None:
            self.suffix_link = self
        else:
            self.suffix_link = self

    def add_link(self, c, v):
        """ Link this node to node v via string c"""
        self.children[c] = v

class SuffixTrie(object):
    def __init__(self):
        self.root = 
