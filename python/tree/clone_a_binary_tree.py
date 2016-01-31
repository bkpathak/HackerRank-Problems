class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def tree_clone(root):
    if root is None:
        return

    left = tree_clone(root.left)
    right = tree_clone(root.right)
    return Node(root.val,left,right)

def in_order_traverse(root):
    if root is None:
        return
    in_order_traverse(root.left)
    print(root.val, end=" ")
    in_order_traverse(root.right)


tree = Node(30, Node(20, Node(15),Node(25)),Node(40,Node(35),Node(50)))

new_tree = tree_clone(tree)
in_order_traverse(new_tree)
print()
