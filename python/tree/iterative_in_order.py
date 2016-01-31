class Node(object):
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traverse(root):
    if root is None:
        return

    stack = []
    current = root
    while(len(stack) > 0 or current):
        if (current):
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.val ,end = " ")
            current = current.right
    print()

tree = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))

in_order_traverse(tree)
