"""
Implementon of Trie for standard English Alphabets
"""

NUM_OF_CHAR = 26
class Node(object):
    def __init__(self):
        self.is_word = False
        self.child = [None] * NUM_OF_CHAR

class Trie(object):
    def __self__(self):
        self.root = Node()

    def insertWord(word):
        temp_branch = root
        for w in word:
            if not temp_branch[ord(w)]:
                temp_branch = temp_branch[ord(w)]
            else:
                temp_branch[ord(w)] = Node()
                temp_branch = temp_branch[ord(w)]

        temp_branch.is_word = True

    def delete(self,word):
        self.delete_helper()
