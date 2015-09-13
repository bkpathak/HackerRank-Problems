class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is not  None:
        mirror_tree(root.left)
        mirror_tree(root.right)

        root.left, root.right = root.right,root.left

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val,sep=" ",end="")
        inorder_traversal(root.right)

if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)

    inorder_traversal(tree)
    mirror_tree(tree)
    print()
    inorder_traversal(tree)
