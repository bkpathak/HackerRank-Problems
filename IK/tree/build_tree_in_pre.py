from collections import deque

class Node(object):
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

val_index = {}

def create_inorder_index(in_order):
    for index,val in enumerate(in_order):
        val_index[val] = index

def index_lookup(val):
    return val_index[val]

def level_order_print(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)

    current_level = 1
    next_level = 0
    while(queue):
        current_node = queue.popleft()
        current_level -= 1
        print(current_node.val, end= " ")

        if current_node.left is not None:
            queue.append(current_node.left)
            next_level += 1
        if current_node.right is not None:
            queue.append(current_node.right)
            next_level += 1

        if current_level == 0:
            current_level = next_level
            next_level = 0
            print()

def build_tree(in_order,pre_order,in_start,in_end, pre_offset):
    if in_start > in_end or pre_offset >= len(pre_order):
        return

    root_index = index_lookup(pre_order[pre_offset])
    left_node = build_tree(in_order,pre_order,in_start,root_index - 1, pre_offset + 1)
    right_node = build_tree(in_order, pre_order,root_index + 1, in_end, pre_offset + (root_index - in_start) + 1 )
    return Node(in_order[root_index], left_node, right_node)

in_order = [5,10,20,30,35,40,45]
pre_order = [30,10,5,20,40,35,45]

create_inorder_index(in_order)
tree = build_tree(in_order, pre_order,0,len(in_order) - 1, 0)
level_order_print(tree)
