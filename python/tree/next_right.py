class Node(object):
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.next_right = None

"""
Solution 1:
Use level order traversal, with integer for each level(0 for root, 1 for
level and so on). Aand set the next_right to point the node from queue, if they
have same node.

Solution 2 (For full binary trees only):
Use preorder traversal to set the next_right of parent before it's child node.
Since the tree is complete,nextRight of p’s left child (p->left->nextRight) will
always be p’s right child, and nextRight of p’s right child
(p->right->nextRight) will always be left child of p’s nextRight
(if p is not the rightmost node at its level).
If p is the rightmost node, then nextRight of p’s right child will be NULL.
"""

def set_next_right(root):
    if root is None:
        return

    # Set the next_right for the root left child
    if(root.left):
        root.left.next_right = root.right

    # If the root.right is right most node set it to None else
    # set it to root.next_right.left
    if(root.right):
        root.right.next_right = root.next_right.left if root.next_right else None

    # recurse for other nodes
    set_next_right(root.left)
    set_next_right(root.right)

def get_next_right(root):
    temp = cp.copy(root)
    while(temp):
        if temp.left:
            return temp.left
        if temp.right:
            return temp.right
        temp = temp.next_right
    return None

def iterative_next_right(root):
    """
    Works for all type of tree
    """
    if root is None:
        return

    # Set the next_right of the root node

    root.next_right = None
    while(root):
        temp_node = root
        while(temp_node):
            if temp_node.left:
                if temp_node.right:
                    temp_node.left.next_right = temp_node.right
                else:
                    temp_node.left.next_right = get_next_right(temp_node)

            if temp_node.right:
                temp_node.right.nextRight = get_next_right(temp_node)
            # Set the next_right for other nodes
            temp_node = temp_node.next_right

        # For the next level
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = get_next_right(root)




def level_order_traverse(root):
    if root is None:
        return
    level_node = cp.copy(root)
    while True:
        print(level_node.val, end = " ")
        if not level_node.next_right:
            print()
            break
        level_node = level_node.next_right
    level_order_traverse(root.left)


tree = Node(1,Node(2,Node(4),Node(5)),Node(3))

#set_next_right(tree)

# level order of tree using next_right pointer
iterative_next_right(tree)

level_order_traverse(tree)
