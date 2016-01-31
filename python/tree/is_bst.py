class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(root,max_val,min_val):
    if root is None:
        return True
    elif ((root.val <= max_val and root.val >= min_val)
        and is_bst(root.left,root.val,min_val)
        and is_bst(root.val,max_val,root.val)
        ):
        return True
    return False


tree = Node(25,Node(10,Node(5),Node(15)),Node(35,Node(30),Node(40)))

min_val = -1 * (2 ** 31)
max_val = (2 ** 31) - 1
print(is_bst(tree,max_val,min_val))
