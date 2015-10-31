def find_kth_elem(tree,k):
    if not tree:
        return

    find_kth_elem(tree.left,k-1)
    if k == 0:
        return root.val
    find_kth_elem(tree.right,k-1)


    
