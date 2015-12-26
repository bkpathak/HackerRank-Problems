# Given array of integer find the contagious subset whose sum to zero.

def sum_zero(arr):
    sum_hash = {}
    r_sum = 0
    for i in range(len(arr)):
        r_sum += arr[i]

        if r_sum == 0 or arr[i] == 0 or r_sum in sum_hash :
            return True
        sum_hash[r_sum] = i
    return False

if __name__ == "__main__":
     arr = [4, 2, -3, 1, 6]
     if sum_zero(arr):
         print("Zero sum is present.")
     else:
         print("Not present.")
