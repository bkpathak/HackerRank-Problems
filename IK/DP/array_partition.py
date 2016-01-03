# https://en.wikipedia.org/wiki/Partition_problem
# http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
# Partition problem is to determine whether a given set can be partitioned into
# two subsets such that the sum of elements in both subsets is same.

# Examples
# arr[] = {1, 5, 11, 5}
# Output: true
# The array can be partitioned as {1, 5, 5} and {11}

# arr[] = {1, 5, 3}
# Output: false
# The array cannot be partitioned into equal sum sets.

# Following are the two main steps to solve this problem:
# 1) Calculate sum of the array. If sum is odd, there can not be
#    two subsets with equal sum, so return false.
# 2) If sum of array elements is even, calculate sum/2 and find a subset of
#    array with sum equal to sum/2.

def is_partitioin_recur(arr,n,part_sum):
    if part_sum == 0:
        return True
    if n == 0 and part_sum != 0:
        return False

    # if last element is greater than sum then ignore it
    if arr[n-1] > part_sum:
        return is_partitioin_recur(arr,n-1,part_sum)

    # Check if sum can be obtained by
    # 1. including the last elemnt
    # 2. excluding the last element

    return is_partitioin_recur(arr,n-1,part_sum) or is_partitioin_recur(arr,n-1,part_sum - arr[n-1])

memo_dict = {}
def is_partitioin_memo(arr,n,part_sum):
    if part_sum == 0:
        return True
    if n == 0 and part_sum != 0:
        return False
    if (n,part_sum) in memo_dict:
        return memo_dict[(n,part_sum)]

    # if last elememt is grater than sum then ignore it
    if arr[n-1] > part_sum:
        return is_partitioin_memo(arr,n-1,part_sum)

    # Check if sum can be obtained by
    # 1. including the last element
    # 2. excluding the last element

    is_true = (is_partitioin_memo(arr,n-1,part_sum) or
                is_partitioin_memo(arr,n-1,part_sum - arr[n-1]))
    memo_dict[(n,part_sum)] = is_true
    return is_true

def is_partitioin_bottomn_up(arr,half_sum):
    arr_len = len(arr)
    P =  [[False] * (half_sum + 1) for i in range(arr_len + 1)]

    # Initialize the top row as True.
    for i in range(arr_len + 1):
        P[i][0] = True

    # Fill the table
    for i in range(1,arr_len + 1):
        for j in range(1, half_sum + 1):
            P[i][j] = P[i-1][j]
            if j >= arr[i-1]:
                P[i][j] = P[i-1][j] or P[i-1][j - arr[i-1]]
    return P[arr_len][half_sum]

def find_partition(arr):
    if len(arr) <= 1 :
        return False

    arr_sum = sum(arr)
    # Return false if sum of array element is odd
    if arr_sum % 2 != 0:
        return False

    #return is_partitioin_recur(arr,len(arr), arr_sum // 2 )
    #return is_partitioin_memo(arr,len(arr), arr_sum // 2)
    return is_partitioin_bottomn_up(arr,arr_sum // 2)

if __name__ == "__main__":
    arr = [[1,5,11,5],[1],[1,5,4,7]]

    for a in arr:
        if find_partition(a):
            print("Array can be partitioned. ",a)
        else:
            print("Array cannot be partitioned. ",a)
