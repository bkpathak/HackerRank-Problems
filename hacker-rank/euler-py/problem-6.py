T=int(input())
for t in range(T):
    N = int(input())
    sum_of_square = N*(N+1)*(2*N+1) / 6
    square_of_sum = (N*(1+N)/2) ** 2
    diff = square_of_sum - sum_of_square
    print(int(diff))
