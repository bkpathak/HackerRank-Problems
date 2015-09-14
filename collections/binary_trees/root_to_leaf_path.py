class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

path = []
def root_to_leaf(root):
    if root is not None:
        path.append(root.val)
        if root.left == None and root.right == None:
            print(" ".join(map(str,path)))
            path.pop()
        else:
            root_to_leaf(root.left)
            root_to_leaf(root.right)
            path.pop()


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)

    root_to_leaf(tree)
