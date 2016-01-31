# The search the 2D array for the target element where array is sorted from
# left to right and top to bottom


def search_2D_array(arr,x):
    row = 0
    col = len(arr[0]) - 1

    while row < len(arr) and col >= 0:
        if arr[col][row] == x:
            return True
        elif arr[row][col] < x:
            row += 1
        else:
            col -= 1
    return False

if __name__ == "__main__":
    arr = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]
          ]

    if search_2D_array(arr,37):
        print("Present in array")
    else:
        print("Not present.")
