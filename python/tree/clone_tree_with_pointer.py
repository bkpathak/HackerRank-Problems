class Node(object):
    def __init__(self, val, left = None, right = None,):
        self.val = val
        self.left = left
        self.right = right
        self.extra_p = None

def clone_tree(tree,node_map):
    if tree == None:
        return
    left = clone_tree(tree.left,node_map)
    right = clone_tree(tree.right,node_map)
    node = Node(tree.val,left,right)
    node_map[tree] = node
    return node


def add_pointer(tree1, tree2,my_map):
    if tree1 == None:
        return
    if tree1.extra_p is not None:
        tree2.extra_p = my_map[tree1.extra_p]

    add_pointer(tree1.left,tree2.left,my_map)
    add_pointer(tree1.right,tree2.right,my_map)

if __name__ == "__main__":
    tree = Node(3,Node(2,Node(1),None),Node(56))
    tree.left.extra_p = tree.right # 2 => 56
    tree.extra_p = tree.left.left # 3 => 1
    my_map = {}
    tree_clone = clone_tree(tree,my_map)

    add_pointer(tree,tree_clone,my_map)

    # Display the pointer
    print(tree_clone.left.extra_p.val) # 56
    print(tree_clone.extra_p.val)      # 1

     # id of the original tree
    print(id(tree.right))

    # id of the node in new tree 1 is pointing
    print(id(tree_clone.left.extra_p))
    # actual id of node 1 is pointing to and this equals to extra_p of node 1
    print(id(tree_clone.right))
