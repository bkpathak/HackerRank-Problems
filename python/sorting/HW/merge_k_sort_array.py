import sys
class HeapNode(object):
    def __init__(self,val,arr_ind,next_elem):
        self.val = val
        self.arr_ind = arr_ind
        self.next_elem = next_elem

    def get_val(self):
        return self.val

    def get_arr_ind(self):
        return self.arr_ind

    def get_next_elem(self):
        return self.next_elem


def heapify(min_heap,K):
    for i in range(K//2 , -1,-1):
        sink(min_heap,i,K)

def sink(min_heap,i,K):
    while((2*i) + 1 < K):
        j = 2 * i + 1

        # Find the minimum betwenn the children
        if(j+1 < K and min_heap[j].get_val() > min_heap[j+1].get_val()):
            j += 1
        # If root is less then children no need to sink
        if(min_heap[i].get_val() < min_heap[j].get_val()):
            break

        # Swap the min of the children with root
        min_heap[i],min_heap[j] = min_heap[j],min_heap[i]
        i = j

def merge_k_array(k_list,K,N):
    min_heap = []
    sorted_array = []
    for i in range(K):
        # Create the new HeapNode
        heap_node = HeapNode(k_list[i][0],i,1)
        min_heap.append(heap_node)

    # Heapify the first K element

    heapify(min_heap,K)
    for i in range(K*N):
        # Get thh curent minimum element from the heap
        min_node = min_heap[0]

        sorted_array.append(min_node.get_val())
        # Add the next element from the array which curent_min belongs
        if (min_node.get_next_elem() < N):
            new_elem = k_list[min_node.get_arr_ind()][min_node.get_next_elem()]
            min_heap[0] = HeapNode(new_elem,min_node.get_arr_ind(),min_node.get_next_elem() + 1)
        # The ccurrent array is scanned completely add maxvlaue as array element
        else:
            min_heap[0] = HeapNode(sys.maxsize,-1,-1)

        #Sink the newly added element to its position
        sink(min_heap,0,K)

    return sorted_array


data = [
        [1,3,5,7],
        [2,4,6,8],
        [0,9,10,11]
        ]
out_arr = merge_k_array(data,3,4)
for i in out_arr:
    print(i,end=",")
print()
