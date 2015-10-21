def swap(num_list,i,j):
    num_list[i],num_list[j] = num_list[j], num_list[i]

def partition(num_list,lo,hi):
    if hi <= lo:
        return
    v = num_list[lo]
    i = lo + 1
    j = hi
    while (True):
        while(num_list[i] < v and i < hi):
            i += 1

        while(num_list[j] > v and j > lo):
            j -= 1

        if ( i >= j):
            break
        swap(num_list,i,j)

    swap(num_list,lo,j)
    return j

def quick_sort(num_list,lo,hi):
    print(num_list)
    if hi <= lo:
        return

    p = partition(num_list, lo,hi)
    quick_sort(num_list, lo, p - 1)
    quick_sort(num_list, p+1, hi)

quick_sort([9,8,7,6,5,4,3,2,1],0,8)
