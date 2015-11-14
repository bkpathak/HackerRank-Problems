class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def find_subtree(root,count):
    if root is None:
        return True

    l_subtree = find_subtree(root.left,count)
    r_subtree = find_subtree(root.right,count)

    if l_subtree and r_subtree:
        left_node = root.left
        right_node = root.right

        # If leaf Node
        if left_node is None and right_node is None:
            count[0] += 1

        # if left and right subtree are unival and if equal to root
        elif left_node and right_node and left_node.val == right_node.val and left_node.val == root.val:
            count[0] += 1

        # If left child exists and equals to root
        elif left_node and left_node.val == root.val:
            count[0] += 1

        # If right child exists and equals to root
        elif right_node and right_node.val == root.val:
            count[0] += 1

        return True

    else:
        return False


def find_unival_subtree(root):
    count = [0]
    find_subtree(root, count)
    return count

tree = Node(5,Node(5,Node(5),Node(5)),Node(5,None,Node(5)))

print(find_unival_subtree(tree)[0])
