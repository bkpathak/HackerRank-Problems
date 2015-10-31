"""
Check if the array contains elements which adds up to the target.
[1,4,7,2] ,10 => 1 + 7 + 2
"""

def arr_element_sum(arr,target):
    arr_element_sum_util(arr,target,0)

def arr_element_sum_util(arr,target,start):
    if target == 0:
        return True
    if start == len(arr):
        return False

    if arr_element_sum_util(arr,target - arr[start],start + 1 ):
        return True
    return arr_element_sum_util(arr,target,start + 1)

print(arr_element_sum([1,4,7,2],10))
