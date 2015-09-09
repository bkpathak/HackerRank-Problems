#Read input from STDIN. Print output to STDOUT
    
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    i = 999
    p = 0
    while i >= 100:
        j = 999
        while j >= i:
            v = i * j
            strv = str(v)
            if v < p: break
            if strv == strv[::-1] and v < N: p = v
            j -= 1 
        i -= 1
    print p
