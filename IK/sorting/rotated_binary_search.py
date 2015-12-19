"""
Given a rotated sorted array, find the first occurrence of a certain number X
with the lowest possible complexity(both time and space).

X = 6
Arr = 8,9,9,1,3,4,4,4,6,6,7,7
Ans = 8
"""

def find_first(arr, x ,ind):
    while ind >= 0 and arr[ind] == arr[ind -1]:
        ind -= 1
    return ind 

def rotated_binary_search(arr, x):
    left = 0
    right = len(arr) -1

    while(left <= right):
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return find_first(arr,x,mid)

        # Bottom half is shorted
        elif arr[left] <= arr[mid]:
            if arr[left] <= x and x <= arr[mid]:
                right = mid -1
            else:
                left = mid +1
        #Upper half is shorted
        else:
            if arr[mid] <= x and x <= arr[right]:
                left = mid +1
            else:
                right = mid - 1

    return -1

if __name__ == "__main__":
    arr = [8,9,9,1,3,4,4,4,6,6,7,7]
    x  = 6
    print(rotated_binary_search(arr,x))
