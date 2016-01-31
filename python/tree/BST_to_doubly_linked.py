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
    tree_to_list(root.left,head,previous)

    # Point the current node left to the previos node
    root.left = previous[0]

    # If previus node exists point it's right to the current node
    # else point the head points to the current node
    if previous[0]:
        previous[0].right = root
    else:
        head[0] = root

    # point current node form head and current node right points back to the
    # head. The head node get automatically updated as the recusrsion folds back.
    current_right = root.right
    head[0].left = root
    root.right = head[0]

    # set the previos node to the current node.
    previous[0] = root

    # traverse the right leaf of the tree.
    tree_to_list(current_right,head, previous)


tree = Node(30, Node(20, Node(15),Node(25)),Node(40,Node(35),Node(50)))

head = [None]
previous = [None]
tree_to_list(tree, previous,head)

temp_head = head[0]
while(temp_head):
    print(temp_head.val)
    temp_head = temp_head.right
    if temp_head is head[0]:
        break
