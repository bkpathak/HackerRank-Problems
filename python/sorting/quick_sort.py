def swap(num_list,i,j):
    num_list[i],num_list[j] = num_list[j], num_list[i]

def partition(num_list,lo,hi):
    if hi <= lo:
        return
    v = num_list[lo]
    i = lo
    j = hi + 1
    while (True):
        i += 1
        while(num_list[i] < v and i < hi):
            i += 1
        j -= 1
        while(num_list[j] > v):
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

quick_sort([1,1,1,1,1,1,1,1,1,1],0,9)
