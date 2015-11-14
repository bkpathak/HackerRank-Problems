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

tree = Node(1,Node(2,Node(4),Node(5)),Node(3))

set_next_right(tree)
