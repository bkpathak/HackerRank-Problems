def merge(num_list,aux,lo,mid,hi):
    for k in range(lo,hi + 1):
        aux[k] = num_list[k]
    i = lo
    j = mid + 1
    for k in range(lo,hi+1):
        if (i > mid):
            num_list[k] = aux[j]
            j += 1
        elif (j > hi):
            num_list[k] = aux[i]
            i += 1
        elif (aux[i] < aux[j]):
            num_list[k] = aux[i]
            i += 1
        else:
            num_list[k] = aux[j]
            j += 1

def merge_sort(num_list,aux,lo,hi):
    print(lo,hi)
    print(num_list)
    if hi <= lo:
        return
    mid = lo + (hi-lo) // 2
    merge_sort(num_list,aux,lo,mid)
    merge_sort(num_list,aux,mid+1,hi)
    merge(num_list,aux,lo,mid,hi)

###############################################################################
# Another technique
##############################################################################

def merge_sort2(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort2(lst[:mid])
    right = merge_sort2(lst[mid:])
    return merge2(left,right)

def merge2(left,right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge2(left[1:],right)
    return [right[0]] + merge2(left,right[1:])
################################################################################

def sort(lst):
    lst_len = len(lst)
    aux = [0] * lst_len
    #merge_sort(lst,aux,0,lst_len-1)
    print(merge_sort2(lst))
    #print(lst)

lst = [9,8,7,6,5,4,3,2,1]
sort(lst)
#print(lst)
