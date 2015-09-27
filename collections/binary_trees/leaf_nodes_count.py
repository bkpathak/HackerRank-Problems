class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def leaf_node_count(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1
    return leaf_node_count(root.left)  + leaf_node_count(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(leaf_node_count(root))
