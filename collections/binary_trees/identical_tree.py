class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def is_identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 != None and root2 != None:
        return (root1.val == root2.val and
        is_identical(root1.left,root2.left) and
        is_identical(root1.right,root2.right))

    return False

tree1 = Node(1)
tree1.left= Node(2)
tree1.right = Node(3)
tree1.left.left = Node(4)

tree2 = Node(1)
tree2.left = Node(2)
tree2.right= Node(10)
tree1.left.left = Node(4)

if is_identical(tree1,tree2):
    print("Tree are IDENTICAL!!")
else:
    print("Tree are NOT IDENTICAL")
