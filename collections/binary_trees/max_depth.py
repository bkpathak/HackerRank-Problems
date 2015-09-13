class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    if root == None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


tree1 = Node(1)
tree1.left= Node(2)
tree1.right = Node(3)
tree1.left.left = Node(4)

print(max_depth(tree1))
