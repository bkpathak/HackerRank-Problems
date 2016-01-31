# Find minumum in rotated array

def find_min(arr):
    left = 0
    right = len(arr) - 1

    while arr[left] > arr[right]:
        mid = left + (right - left)//2
        if arr[mid] < arr[right]:
            right = mid
        else:
            left = mid + 1

    return arr[left]

if __name__ == "__main__":
    arr = [8,9,9,1,3,4,4,4,6,6,7,7]
    print(find_min(arr))
