# Finds the maximum difference in array element

def max_diff_array(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array
    max_diff = 0
    min = array[0]
    max = array[0]
    for n in array:
        if n > max:
            max = n
        if n < min:
            min = n
    return max - min

print(max_diff_array([15,20,2,3,1,16,4]))
