# Finds the height of the binary tree
# Height of the Node: The number of edges in longest path from the node to
# the leaf node.
# Height of the tree: Height of the node

class Node(object):
    def __init__(self,val, left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def find_height_of_tree(tree):
    if tree is None:
        return -1

    left_height = find_height_of_tree(tree.left)
    right_height = find_height_of_tree(tree.right)
    return 1 + max(left_height, right_height)

if __name__ == "__main__":
    tree = Node(1,Node(2,Node(4),Node(5,Node(8),Node(9))),Node(3,Node(8),Node(9)))
    print("Height of the tree is: ", find_height_of_tree(tree))
