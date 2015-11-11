class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find_lca(root,val1, val2):
    if root is None:
        return
    elif root.val == val1 or root.val == val2:
        return root

    left = find_lca(root.left, val1, val2)
    right = find_lca(root.right, val1, val2)

    if left and right:
        return root
    return left if left else right

tree = Node(45,
            Node(25, Node(15,Node(10),Node(20)),Node(30)),
            Node(65, Node(55,Node(50),Node(60)),Node(75,None,Node(80))))

print(find_lca(tree,10,20).val)
print(find_lca(tree,50,80).val)
print(find_lca(tree,20,60).val)
