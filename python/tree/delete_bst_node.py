# Delete the node from the tree
# Approach
# If node is leaf Node: Detach the node and update the deletd parent child with
# null
# Node to be deleted with only one Node: Connect the parent with chile and
# remove the node
# Node to be deletd having two child: Replace the mode to be deletd with the
# minimum value from the right of the node and delete that node recursively

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val= val
        self.left = left
        self.right = right

def find_minimum(root):
    if root.left is None:
        return root.val
    return find_minimum(root.left)

def delete_node(root, node_val):
    if root is None:
        return root
    if node_val < root.val:
        root.left = delete_node(root.left, node_val)
    elif node_val > root.val:
        root.right = delete_node(root.right, node_val)
    else:
        # Found the node now check for the three casee
        # Case 1: leaf Node
        if root.left == None and root.right == None:
            root = None

        # Case 2: One Child
        elif root.left == None:
            root = root.right

        elif root.right == None:
            root = root.left

        else:
            # case 3: 2 child
            min_node = find_minimum(root.right)
            root.val = min_node
            root.right = delete_node(root.right, min_node)
    return root

def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.val, end = " ")
    in_order_traversal(root.right)

if __name__ == "__main__":
    tree = Node(12,
                Node(5,Node(3,Node(1)),Node(7,Node(9))),
                Node(15,Node(13),Node(17)))
    print("Before deleting node 15")
    in_order_traversal(tree)
    delete_node(tree,17)
    print()
    print("After deletion of node 15")
    in_order_traversal(tree)
    print()
