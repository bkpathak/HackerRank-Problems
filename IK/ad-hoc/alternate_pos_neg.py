# Given and array containing both positive and negative numbers, return and array
# of alternating positive and negative integers such that set of integers are in same
# order as in the input array (stable).

"""
Method 1:
Use additional space and two pointer left and right
"""

def alternate_pos_neg(input_arr):
    result = []
    pos = -1
    neg = -1
    while True:
        pos += 1
        while pos < len(input_arr) and input_arr[pos] < 0:
            pos += 1
        if pos < len(input_arr):
            result.append(input_arr[pos])

        neg += 1
        while neg < len(input_arr) and input_arr[neg] >= 0:
            neg += 1
        if neg < len(input_arr):
            result.append(input_arr[neg])

        if len(result) == len(input_arr):
            break
    return result

"""
Method 2:
O(N) => N^2
"""
def alternate_pos_neg1(in_arr):
    for i in range(in_arr):
        j = 0
        while j+2 < len(in_arr):
            S = [in_arr[j], in_arr[j+1], in_arr[j+2]]
            S = [1 if x>= 0 else -1 for x in S]
            if S[0] == S[1] and S[1] != S[2]:
                in_arr[j + 1],in_arr[j+2] = in_arr[j+2], in_arr[j+1]
        j += 1

if __name__ == "__main__":
    input_arr = [2,3,-4,-9,-1,-7,1,-5,-6]
    print("Original Arr: ", input_arr)
    result = alternate_pos_neg(input_arr)
    print("Alternating Arr: ", result)
