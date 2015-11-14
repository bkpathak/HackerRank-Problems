class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traverse(root):
    if root is None:
        return
    in_order_traverse(root.left)
    print(root.val,end = " ")
    in_order_traverse(root.right)

def flip_tree(root):
    if root is None:
        return

    # Traverse recusrsively to the leaf and flip the tree bottom up
    left_node = flip_tree(root.left)
    right_node = flip_tree(root.right)

    left_node, right_node = right_node, left_node
    return Node(root.val,left_node,right_node)

tree = Node(30, Node(20, Node(15),Node(25)),Node(40,Node(35),Node(50)))

print("Original Tree")
in_order_traverse(tree)

print()
print("After Flipping")
new_tree = flip_tree(tree)
in_order_traverse(new_tree)

print()
