# Enter your code here. Read input from STDIN. Print output to STDOUT

def partition(arr,lo,hi,pivot):
    i , j = lo,hi + 1
    # swap the bolt with arr[lo]
    arr[lo], arr[pivot] = arr[pivot], arr[lo]
    v = arr[lo]
    while(True):
        i += 1
        while(arr[i] < v and i < hi):
            i += 1
        j -= 1
        while(arr[j] > v):
            j -= 1
        if i >= j:
            break
        arr[i],arr[j] = arr[j],arr[i]

    arr[lo],arr[j] = arr[j],arr[lo]
    return j

def find_bolts(nuts,bolts,lo,hi):
    if lo >= hi:
        return
    pivot = partition(nuts,lo,hi,lo)
    # partion the bolt taking nut as pivot
    partition(bolts,lo,hi,pivot)

    find_bolts(nuts,bolts,lo,pivot - 1)
    find_bolts(nuts,bolts,pivot + 1,hi)

def match(nuts,bolts):
    if len(nuts) <= 1:
        return
    find_bolts(nuts,bolts,0,len(nuts) - 1)

nuts = ['N3','N2','N1','N4']
bolts = ['B4','B2','B3','B1']

match(nuts,bolts)

for n,b in zip(nuts,bolts):
    print(n,b)
