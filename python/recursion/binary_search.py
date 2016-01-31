# Recursion
def binary_search(n_list,start,end,x):
    if start > end :
        return -1
    mid = start + (end - start) // 2
    if x == n_list[mid]:
        return mid
    elif x > n_list[mid]:
        return binary_search(n_list,mid+1,end,x)
    else:
        return binary_search(n_list,start,mid-1,x)

# Iterative
def binary_search1(n_list,x):
    start = 0
    end = len(n_list) - 1
    while(start <= end):
        mid = start + (end - start) // 2
        if x == n_list[mid]:
            return mid
        elif x < n_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10],0,9,10))
