class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def children_sum(root):
    if root == None or (root.left == None and root.right == None):
        return 0
    # if either left or right node is None use the value as 0.
    left_val  = 0
    right_val = 0

    if (root.left is not None):
        left_val = root.left.val
    if (root.right is not None):
        right_val = root.right.val

    if (root.val == left_val + right_val and children_sum(root.left) and children_sum(root.right)):
        return True
    else:
        return False

root = Node(10)
root.left = Node(6)
root.right = Node(4)

root.left.left = Node(4)
root.left.right = Node(2)

root.right.left = Node(2)
root.right.left = Node(2)
root.right.left.left = Node(2)

if (children_sum(root)):
    print("Root is the sum of children.")
else:
    print("Root is not the sum of children.")
