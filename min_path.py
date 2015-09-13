memo = [-1 for i in range(1001)]
def min_steps(n):
    print(n)
    if n == 1:
        return 0
    n = int(n)
    if memo[n] != -1:
        return memo[n]
    r = 1 + min_steps(n-1)
    if n % 2 == 0:
        r = min(r, 1 + min_steps(n / 2))
    if n % 3 == 0:
        r = min(r,1 + min_steps(n / 3))
    memo[n] = r
    return r

n = int(input("Enter number n >= 1: "))
print(min_steps(n))
