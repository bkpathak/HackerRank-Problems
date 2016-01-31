# Longest Span with same Sum in two Binary arrays
# Given two binary arrays arr1[] and arr2[] of same size n.
# Find length of the longest common span (i, j) where j >= i
# such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1]
# + …. + arr2[j].

"""
Input: arr1[] = {0, 1, 0, 0, 0, 0};
       arr2[] = {1, 0, 1, 0, 0, 1};
Output: 4
The longest span with same sun is from index 1 to 4.
"""

def longest_common_sum_span(arr1, arr2):
    max_len = 0
    pre_sum1 = 0
    pre_sum2 = 0
    arr_len = len(arr1) - 1
    diff = [-1 for i in range(2 * arr_len + 1)]
    for i in range(len(arr1)):
        pre_sum1 += arr1[i]
        pre_sum2 += arr2[i]

        curr_diff = pre_sum1 - pre_sum2
        diff_index = arr_len + curr_diff

        # if current diff is 0, then there are same number of 1's
        # so far. i.e i+1 is the span
        if curr_diff == 0:
            max_len = i + 1

        # If current diff is seen first time, then update the starting index
        # of diff

        elif diff[diff_index] == -1:
            diff[diff_index] = i

        else:
            # find the length of thuis same same common span
            span_len = i - diff[diff_index]

            if span_len > max_len:
                max_len = span_len

    return max_len

if __name__ == "__main__":
    arr1 = [0, 1, 0, 1, 1, 1, 1]
    arr2 = [1, 1, 1, 1, 1, 0, 1]
    print("Common span with same sum is: ",
    longest_common_sum_span(arr1,arr2))
