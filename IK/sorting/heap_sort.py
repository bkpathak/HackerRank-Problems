
def heapify(input_arr, n):
    for i in range( n // 2, -1, -1):
        heap_sink(input_arr,i,n)

def heap_sink(input_arr, i, n):
    # The wrong output was because of this line instead of less then I should have
    # used less then or eueal to (<=)
    while (2 * i) + 1 <= n:
        j = 2* i + 1
        # compare the two child of the node
        if (j + 1) <= n and input_arr[j] > input_arr[j + 1]:
            j += 1
        if input_arr[i] < input_arr[j]:
            break
        # swap the root with smallest child
        input_arr[i],input_arr[j] = input_arr[j],input_arr[i]
        # update i
        i = j


def heap_sort(input_arr):
    if len(input_arr) <= 1:
        return

    # heapify the input_arr
    result = []
    arr_len = len(input_arr) - 1
    heapify(input_arr, arr_len)

    index = 0

    while index < arr_len:
        result.append(input_arr[0])
        # Should have decrease the heap_size after taking root from the heap
        input_arr[0] = input_arr[arr_len - index]
        index += 1
        # Should have decrease the heap_size after taking root from the heap
        heap_sink(input_arr,0,arr_len - index )

    result.append(input_arr[0])

    return result


def heap_sort_inplace(input_arr):
    if len(input_arr) <= 1:
        return
    # heapify the input arr
    arr_len = len(input_arr) - 1
    heapify(input_arr, arr_len)

    while arr_len > 0:
        input_arr[0] , input_arr[arr_len] = input_arr[arr_len], input_arr[0]
        arr_len -= 1
        heap_sink(input_arr,0,arr_len)



if __name__ == "__main__":
    input_data = ["9876543210","454685893","36847954457870"]

    for arr in input_data:
        arr = list(map(int,list(arr)))
        print(heap_sort(arr))

    # Inplcae sort
    # Min heap gives us Descending order
    # If we want ascending order we can use max_heap
    print("Inplcae sort")
    for arr in input_data:
        arr = list(map(int,list(arr)))
        heap_sort_inplace(arr)
        print(arr)
