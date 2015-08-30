T=int(input())
for t in range(T):
    N = int(input())
    smallest_multiple = N
    while True:
        for i in range(1,N+1):
            if smallest_multiple % i != 0: break
        if i == N:
            print(smallest_multiple)
            break
        smallest_multiple += N
                    
            
