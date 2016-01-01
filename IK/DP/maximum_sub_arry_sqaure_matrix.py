# Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
# http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

def find_sub_matrix_recur(arr,i,j,m,n):
    if i < 0 or j < 0:
        return 0
    elif i == 0 or j == 0:
        return arr[i][j]

    max_size = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j]:
                new_res = arr[i][j] + min(find_sub_matrix(arr,i-1,j-1,i,j),
                                        find_sub_matrix(arr,i-1,j,i,j),
                                        find_sub_matrix(arr,i,j-1,i,j))
            else:
                new_res = 0
            max_size = max(max_size,new_res)
    return max_size


memo_dict = {}
def find_sub_matrix_memo(arr,i,j,m,n):
    if i < 0 or j < 0:
        return 0
    elif i == 0 or j == 0:
        return arr[i][j]
    elif (m,n) in memo_dict:
        return memo_dict[(m,n)]
    max_size = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j]:
                new_res = arr[i][j] + min(find_sub_matrix_memo(arr,i-1,j-1,i,j),
                                            find_sub_matrix_memo(arr,i-1,j,i,j),
                                            find_sub_matrix_memo(arr,i,j-1,i,j))
            else:
                new_res = 0
            max_size = max(max_size,new_res)
    memo_dict[(m,n)] = max_size
    return max_size

def find_sub_matrix_bottom_up(arr,m,n):

    # Create the new array
    S  = [[0] * n for i in range(m)]
    # Set the first row
    for i in range(n):
        S[0][i] = arr[0][i]
    # Set the first column
    for i in range(m):
        S[i][0] = arr[i][0]

    max_size = 0
    for i in range(1,m):
        for j in range(1,n):
            if arr[i][j]:
                S[i][j] = 1 + min(S[i-1][j-1],S[i-1][j],S[i][j-1])
            else:
                S[i][j] = 0
            max_size = max(max_size,S[i][j])

    return max_size

if __name__ == "__main__":
    arr = [[0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]]

    # print(find_sub_matrix_mem(arr,1,1,6,5))
    # print(find_sub_matrix_recur(arr,1,1,6,5))
    print(find_sub_matrix_bottom_up(arr,6,5))
