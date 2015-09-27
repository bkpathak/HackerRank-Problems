class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

#Only works when both of the nodes are present in the tree.
def least_com_ancestor1(root,n1,n2):
    if root is None:
        return None
    if root.val == n1 or root.val == n2:
        return root

    left = least_com_ancestor(root.left,n1,n2)
    right = least_com_ancestor(root.right,n1,n2)

    if left and right:
        return root

    return root if left else right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(least_com_ancestor(root,10,11).val)
