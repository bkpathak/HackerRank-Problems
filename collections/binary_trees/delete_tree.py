'''
There is nothing similar in Python as in C/C++ of freeing the pointer.
One of the way to do it in the Python is to stop referencing the Node which is
no longer used.
'''

class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def delete_tree(root):
    if root is not None:
        delete_tree(root.left)
        delete_tree(root.right)

        print("Deleting the Node with val: ", root.val)
        root.left = root.right = None


tree1 = Node(1)
tree1.left= Node(2)
tree1.right = Node(3)
tree1.left.left = Node(4)

delete_tree(tree1)
