# Given Array containing both positive and negative array
# find the sum of maximum sub array and the index

def max_sum_sub_array(array):
    current_sum = array[0]
    max_sum = array[0]
    start_ind = end_index = temp_index = 0

    for i in range(1,len(array)):
        if array[i] > (current_sum + array[i]):
            current_sum = array[i]
            temp_index = i
        else:
            current_sum += array[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_ind = temp_index
            end_index = i

    return max_sum, start_ind, end_index

if __name__ == "__main__":
    array = [1,-3,2,-5,7,6,-1,-4,11,-23]
    print(max_sum_sub_array(array))
