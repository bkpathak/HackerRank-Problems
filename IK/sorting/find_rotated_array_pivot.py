def rotated_array_pivot(arr):
    left = 0
    right = len(arr) - 1

    while arr[left] > arr[right]:
        mid = left + (right -left) // 2
        # pivot is is right
        if arr[mid] > arr[right]:
             left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    arr = [8,9,9,1,3,4,4,4,6,6,7,7]
    print(rotated_array_pivot(arr))
