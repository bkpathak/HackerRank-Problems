# Enter your code here. Read input from STDIN. Print output to STDOUT
def swap(num_list,i,j):
    num_list[i],num_list[j] = num_list[j], num_list[i]

def partition(arr,lo,hi):
    i = lo
    j = hi + 1
    v = arr[lo]
    while True:
        i += 1
        while(arr[i] < v and i < hi):
            i += 1
        j -= 1
        while(arr[j] > v):
            j -= 1
        if i >= j:
            break
        swap(arr,i,j)
    swap(arr,lo,j)

    return j

def select(arr,left,right,kth):
    pivot = partition(arr,left,right)
    pos = pivot - left + 1
    if pos == kth:
        return arr[pivot]
    if kth < pos:
        return select(arr,left,pivot - 1,kth)
    else:
        return select(arr,pivot + 1,right,kth - pos)

def find_median(arr):
    arr_len = len(arr)
    return select(arr,0,arr_len - 1, arr_len // 2)

data = ['123528473','345357645554','345435656324546','678675645342354657','2435435464']
for d in data:
    print(find_median(list(d)))
