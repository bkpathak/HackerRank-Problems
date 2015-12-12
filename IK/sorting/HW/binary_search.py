# Binary search

def recursive_search(array,lo,hi,x):
    if hi <= lo:
        return -1

    mid = lo + (hi - lo) // 2
    if array[mid] == x:
        return mid
    elif array[mid] > x:
        return recursive_search(array,lo,mid-1,x)
    else:
        return recursive_search(array,mid + 1,hi,x)
