class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def tree_size(root):
    if root == None:
        return 0
    else:
        return (tree_size(root.left) + 1 + tree_size(root.right))

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print(tree_size(tree))
