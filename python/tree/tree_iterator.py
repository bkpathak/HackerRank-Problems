"""
Create in_order iterator for tree.
"""
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TreeIterator(object):
    def __init__(self,root = None):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self):
        current_node = self.stack.pop()
        next_val = current_node.val

        if (current_node.right):
            current_node = current_node.right
            while current_node:
                self.stack.append(current_node)
                current_node = current_node.left

        return next_val

    def has_next(self):
        return True if len(self.stack) >= 1 else False

tree = Node(45,
            Node(25, Node(15,Node(10),Node(20)),Node(30)),
            Node(65, Node(55,Node(50),Node(60)),Node(75,None,Node(80))))

iterator = TreeIterator(tree)


# Print all the node of the tree using iterator
while(iterator.has_next()):
    print(iterator.next())
