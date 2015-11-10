"""
Create balanced tree from the sorted array.
"""
from collections import deque

class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(list,start,end):
    if start > end:
        return

    mid = start + (end - start) // 2

    left_tree = create_tree(list,start,mid-1)
    right_tree = create_tree(list,mid + 1, end)

    root = Node(list[mid],left_tree,right_tree)
    return root

def level_order_print(root):
    queue = deque()
    queue.append(root)
    current_level = 1
    next_level = 0
    while(queue):
        current_node = queue.popleft()
        current_level -= 1
        print (current_node.val,end=" ")

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

arr = [1,2,3,4]

tree = create_tree(arr,0,len(arr) - 1)

level_order_print(tree)
