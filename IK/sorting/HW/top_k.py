# Complete the function below.
def heapify(min_heap,N):
    for k in range( N // 2,-1,-1):
        sink(min_heap,k,N)

def sink(min_heap,k,N):
    while((2 * k) + 1 < N):
        j = 2 * k + 1
        if(j+1 < N and min_heap[j] > min_heap[j+1]):
            j += 1
        if(min_heap[k] < min_heap[j]):
            break
        min_heap[k],min_heap[j] = min_heap[j], min_heap[k]
        k = j


def  topK( iStream,  iK):
    min_heap = []

    # Add first K element to heap.
    for i in range(iK):
        min_heap.append(iStream[i])

    # Heapify the min_heap
    heapify(min_heap,iK)

    for i in range(iK,len(iStream)):
        if iStream[i] > min_heap[0]:
            min_heap[0] = iStream[i]
            # sink the newly added element to it proper position
            sink(min_heap,0,iK)
    # Sorted the final array to pass the test case
    return sorted(min_heap,reverse=True)
