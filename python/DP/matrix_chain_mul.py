# http://www.columbia.edu/~cs2035/courses/csor4231.F15/matrix-chain.pdf
# http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
# Given a sequence of matrices, find the most efficient way to multiply these
# matrices together. The problem is not actually to perform the multiplications,
# but merely to decide in which order to perform the multiplications.

# We have many options to multiply a chain of matrices because matrix
# multiplication is associative. In other words, no matter how we parenthesize
# the product, the result will be the same. For example, if we had four matrices
# A, B, C, and D, we would have:

#     (ABC)D = (AB)(CD) = A(BCD) = ....
# However, the order in which we parenthesize the product affects the number of
# simple arithmetic operations needed to compute the product, or the efficiency.
# For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix,
# and C is a 5 × 60 matrix. Then,

#    (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
#    A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
# Clearly the first parenthesization requires less number of operations.

# Given an array p[] which represents the chain of matrices such that the ith
# matrix Ai is of dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder()
# that should return the minimum number of multiplications needed to multiply the chain.

import time

def find_optimal_chain(arr, i, j):
    if i == j:
        return 0
    min_val = 2 ** 32 - 1
    for k in range(i,j):
        count = (find_optimal_chain(arr,i,k) + find_optimal_chain(arr,k + 1,j) +
                arr[i-1] * arr[k] * arr[j])
        min_val = min(count,min_val)
    return min_val

dict_memo = {}
def find_optimal_chain_memo(arr,i,j):
    if i == j:
        return 0
    if (i,j) in dict_memo:
        return dict_memo[(i,j)]

    min_val = 2 ** 32 - 1
    for k in range(i,j):
        count = (find_optimal_chain_memo(arr,i,k) + find_optimal_chain_memo(arr,k + 1,j) +
                arr[i-1] * arr[k] * arr[j])

        min_val = min(count,min_val)
    dict_memo[(i,j)] = min_val
    return min_val

def find_optimal_chain_bottom_up(arr):
    n = len(arr)
    M = [[0] * n  for i in range(n)]

    for l in range(2,n):
        for i in range(0,n-l):
            j = i + l
            M[i][j] = 2 ** 31
            for k in range(i + 1,j):
                count = M[i][k] + M[k][j] + arr[i] * arr[k] * arr[j]
                M[i][j] = min(count,M[i][j])
    return M[0][n-1]


if __name__ == "__main__":
    start = time.time()
    arr = [1,2,3,4]
    print(find_optimal_chain(arr,1,len(arr) - 1))
    print(find_optimal_chain_memo(arr,1,len(arr) - 1))
    print(find_optimal_chain_bottom_up(arr))
    print("Elapsed Time: ", time.time() - start)
