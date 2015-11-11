class Node(object):
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def root_to_leaf(root,path):
    if root.left is None and root.right is None:
        path.append(root.val)
        print(" ".join(map(str,path)))
        return

    path.append(root.val)
    root_to_leaf(root.left, path)
    path.pop()
    root_to_leaf(root.right, path)
    path.pop()

tree = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))

root_to_leaf(tree,[])
