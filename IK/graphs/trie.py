# Implementon of Trie for standard English Alphabets
# http://www.geeksforgeeks.org/trie-delete/

NUM_OF_CHAR = 26
class Node(object):
    def __init__(self):
        self.is_word = False
        self.child = [None] * NUM_OF_CHAR


class Trie(object):
    def __init__(self):
        self.root = Node()

    # Helper function to find the index of the char
    def index(self,char):
        return ord(char) - ord("a")


    def insertWord(self,word):
        word = word.lower()
        temp_branch = self.root
        for w in word:
            ind = self.index(w)
            if temp_branch.child[ind]:
                temp_branch = temp_branch.child[ind]
            else:
                temp_branch.child[ind] = Node()
                temp_branch = temp_branch.child[ind]

        temp_branch.is_word = True


    def search(self,key):
        """
        Search for the key in trie.
        """
        if key == "":
            raise ValueError("Key Empty")

        start = self.root
        for k in key:
            ind = self.index(k)
            if not start.child[ind]:
                return False
            start = start.child[ind]
        return True


    def delete(self,key):
        start = self.root
        self.delete_helper(self, start, key,0)

    def delete_helper(self,root, key,pos):
        """
        The following are possible conditions when deleting key from trie,
        1. Key may not be there in trie. Delete operation should not modify trie.
        2. Key present as unique key (no part of key contains another key (prefix),
            nor the key itself is prefix of another key in trie). Delete all the nodes.
        3. Key is prefix key of another long key in trie. Unmark the leaf node.
        4. Key present in trie, having atleast one other key as prefix key. Delete
            nodes from end of key until first leaf node of longest prefix key.
        """
        if root is not None:
            # Base Case
            if pos == len(key):
                if root.is_word:
                    root.is_word = False
                    if self.has_child_node(root):
                        return True
                    else:
                        False
            # Recursive case
            else:
                ind = self.index(key[pos])
                if self.delete_helper(root.child[ind],pos + 1):
                    # Last node in key delete it
                    root[ind] = None
                    # recursively delete the upper eligible nodes
                    return not self.has_child_node(root) and not root.is_word
    def has_any_child(self,root):
        for i in NUM_OF_CHAR:
            if root[i] is not None:
                return True

if __name__ == "__main__":
    trie = Trie()
    trie.insertWord("an")
    trie.insertWord("ann")
    trie.insertWord("anne")
    trie.insertWord("to")
    trie.insertWord("ton")
    if trie.search("ann"):
        print("present")
