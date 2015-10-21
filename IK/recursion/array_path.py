"""
Find the total number of path in arry.
Only right and down movement is allowed.
Constraint: a[i][j] shoukd be 1 to be valid path
"""

def array_path(arr,i,j):
    if not arr[i][j]:
        return 0

    elif i == len(arr) - 1 and j == len(arr[0]) - 1:
         return 1

    if i < len(arr)-1 and j < len(arr[0]) - 1:
        return array_path(arr,i + 1,j) + array_path(arr,i,j + 1)

    elif i == len(arr)-1:
        return array_path(arr,i,j+1)

    elif j == len(arr[0])-1:
        return array_path(arr,i+1,j)

print(array_path([[1,1,1],[1,1,1],[1,1,1]],0,0))
