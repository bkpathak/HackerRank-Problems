"""
Merge two BST.
Tree1: 2 -> 1,3
Tree2: 7 -> 6,8

Approach:
1. Traverse in-order both the tree.
2. Merge the in-order Traverse
3. Ceate the BST from the merge tree
"""
from collections import deque

class Node(object):
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traverse(root,arr):
    if root is None:
        return
    in_order_traverse(root.left,arr)
    arr.append(root.val)
    in_order_traverse(root.right,arr)
    return arr

def merge_array(arr1,arr2):
    merge_arr = []
    i, j = 0, 0
    hi = len(arr1) + len(arr2)
    for k in range(0,hi):
        if i >= len(arr1):
            merge_arr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            merge_arr.append(arr1[i])
            i += 1
        elif arr1[i] < arr2[j]:
            merge_arr.append(arr1[i])
            i += 1
        else:
            merge_arr.append(arr2[j])
            j += 1
    return merge_arr

def create_tree(list,start,end):
    if start > end:
        return

    mid = start + (end - start) // 2

    left_tree = create_tree(list,start, mid - 1)
    right_tree = create_tree(list, mid + 1, end)
    return Node(list[mid], left_tree, right_tree)

def level_order_traverse(root):
    if root is None:
        return

    queue = deque()

    queue.append(root)
    current_level = 1
    next_level = 0

    while(queue):
        current_node = queue.popleft()
        current_level -= 1
        print(current_node.val, end = " ")

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

tree1 = Node(2,Node(1),Node(3))
tree2 = Node(7,Node(6),Node(8))

in_order_arr1 = in_order_traverse(tree1, [])
print(in_order_arr1)
in_order_arr2 = in_order_traverse(tree2, [])
print(in_order_arr2)
merge_arr = merge_array(in_order_arr1,in_order_arr2)

print(merge_arr)

tree = create_tree(merge_arr,0 , len(merge_arr) - 1)

level_order_traverse(tree)
