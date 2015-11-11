"""
Iterative post order tree traverse
"""

class Node(object):
    def __init__(self,val,left =None, right = None):
        self.val = val
        self.left = left
        self.right = right

def iterative_post_order(root):
    if root is None:
        return

    stack = []
    stack.append(root)
    while(len(stack) > 0):
        current_node = stack.pop()
        print(current_node.val,end = " ")
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)
    print()

tree = Node(2,Node(1,Node(5),Node(6)),Node(3))

iterative_post_order(tree)
