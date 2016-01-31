class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find_largest_BST_subtree(root,min_val,max_val, max_nodes, largest_BST):
    """
    Largest subtree must contains all the descendants of the tree.
    """
    if root is None:
        return 0

    isBST = True
    left_nodes = find_largest_BST_subtree(root.left, min_val,
                  max_val ,max_nodes,largest_BST)
    curr_min = root.val if left_nodes == 0 else min_val[0]
    if left_nodes == -1 or (left_nodes != 0 and root.val <= max_val[0] ):
        isBST = False

    right_nodes = find_largest_BST_subtree(root.right, min_val,
                  max_val, max_nodes, largest_BST)
    curr_max = root.val if right_nodes == 0 else max_val[0]
    if right_nodes == -1 or (right_nodes != 0 and root.val >= min_val[0]):
        isBST = False

    if (isBST):
        min_val[0] = curr_min
        max_val[0] = curr_max
        total_nodes = left_nodes + right_nodes + 1
        if total_nodes > max_nodes[0]:
            max_nodes[0] = total_nodes
            largest_BST[0] = root
        return total_nodes
    else:
        return -1

def traverse_tree(root):
    if root is None:
        return
    traverse_tree(root.left)
    print(root.val, end = " ")
    traverse_tree(root.right)

def find_BST_subtree(root):
    min_val = [-1 * (2 ** 31)]
    max_val = [(2 ** 31) - 1]
    max_nodes = [min_val[0]]
    largest_BST = [None]

    find_largest_BST_subtree(root,min_val, max_val, max_nodes, largest_BST)
    print(max_nodes[0])
    print("Inorder traverse of largest BST:")
    traverse_tree(largest_BST[0])
    print()

tree = Node(10, Node(5, Node(1), Node(8)), Node(15,None,Node(7)))
find_BST_subtree(tree)
