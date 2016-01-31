class Node(object):
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def post_order_traverse(root):
    if root is None:
        return

    stack = [root]
    previous_node = None
    while(len(stack) > 0):
        current_node = stack[-1]
        if(not previous_node or previous_node.left ==current_node or previous_node.right == current_node):
            if current_node.left:
                stack.append(current_node.left)
            elif current_node.right:
                stack.append(current_node.right)

        elif current_node.left == previous_node:
            if current_node.right:
                stack.append(current_node.right)

        else:
            print(current_node.val,end = " ")
            stack.pop()

        previous_node = current_node

    print()

tree = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))

post_order_traverse(tree)
