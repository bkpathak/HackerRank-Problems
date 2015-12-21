"""
Given an array of n elements, where each element is at most k away
from its target position, devise an algorithm that fully sorts the array, in approximately O(n log k) time.
"""
"""
arr = [3,2,1,4,7,6,8]
k = 2

min_heap = 2 => 3

"""
# min_heap => array

def heapify(min_heap,heap_size):
    for i in range( heap_size // 2 , -1, -1):
        # Sink the element at index i
        sink(min_heap, i,heap_size)

def sink(min_heap,i,heap_size):
    while (2 * i) + 1 < heap_size:
        j = 2 * i + 1
        if j + 1 < heap_size and min_heap[j] > min_heap[j +1]:
            j += 1
        # No need to sink root is already minimum then it's child
        if min_heap[i] < min_heap[j]:
            break

        # swap the root with minimum of it's child
        min_heap[i] , min_heap[j] = min_heap[j] , min_heap[i]
        i = j


def sort_arr(arr,k):
    # create min_heap with first k element
    min_heap = []
    heap_size = k + 1
    for i in range(heap_size):
        min_heap.append(arr[i])

    # Heapify the min heap
    heapify(min_heap, heap_size)

    # Now take the root of the min_heap and add the new element from array
    index  = 0
    for new_elem in range(heap_size,len(arr)):
        # put the root of the node
        arr[index] = min_heap[0]
        index += 1
        # add new element to heap
        min_heap[0] = arr[new_elem]
        # sink the root
        sink(min_heap,0,heap_size)

    while index < len(arr):
        arr[index] = min_heap[0]
        # put int max to the root of the min_heap
        min_heap[0] = 2 ** 32
        index += 1
        sink(min_heap,0,heap_size)

if __name__ == "__main__":
    k = [3,2]
    data = [[2, 6, 3, 12, 56, 8], [3,2,1,4,7,6,8]]
    for i,d in enumerate(data):
        print("Before Sort: " , d)
        sort_arr(d,k[i])
        print("After Sort", d)
