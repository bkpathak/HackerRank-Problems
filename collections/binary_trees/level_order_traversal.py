import collections

class Node(object):
    def __init__(self,x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right

def level_order_traversal(root):
    if root is None:
        return
    queue = collections.deque([root])
    current_level, next_level = 1,0
    while len(queue) != 0:
        current_node = queue.popleft()
        current_level -= 1
        print(current_node.val,end='')
        if current_node.left:
            queue.append(current_node.left)
            next_level += 1
        if current_node.right:
            queue.append(current_node.right)
            next_level += 1
        if current_level == 0:
            print()
            current_level,next_level = next_level,current_level

tree = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))
level_order_traversal(tree)
