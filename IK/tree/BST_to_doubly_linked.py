"""
Great Tree Recursion Problem.
One of the interesting tree problem came so far.
http://cslibrary.stanford.edu/109/TreeListRecursion.html
"""
import copy as cp
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root,head,previous):
    if root is None:
        return
    # Travel all the way to left most node of the tree
    tee_to_list(root.left,head,previous)

    # Point the current node left to the previos node
    root.left = previous

    # If previus node exists point it's right to the current node
    # else point the head points to the current node
    if previous:
        previous.right = root
    else:
        head = cp.copy(root)

    # point current node form head and current node right points back to the
    # head. The head node get automatically updated as the recusrsion folds back.
    current_right = root.right
    head.left = root
    root.right = head

    # set the previos node to the current node.
    previous = root

    # traverse the right leaf of the tree.
    tree_to_list(current_right,head, previous)


tree = Node(30, Node(20, Node(15),Node(25)),Node(40,Node(35),Node(50)))

head = conver_to_doubly(tree,None,None)

while(head):
    print(head.val)
    head = head.right
