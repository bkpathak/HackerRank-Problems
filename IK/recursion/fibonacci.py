"""
Time: O(n) = 2 ^ n (Linear O(n) for iterative )
Space: O(n) = depth of the recursion tree
"""
import timeit
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib (n-2)

## with memoization
def fib_m(n,memo={}):
    if n <= 1:
        return n
    try:
    #if n in memo:
        return memo[n]
    #else:
    except KeyError:
        result = fib_m(n-1) + fib_m(n-2)
        memo[n] = result
        return result

start = timeit.timeit()
print(fib(20))
end = timeit.timeit()
print("fib time: " ,start - end)
start = timeit.timeit()
print(fib_m(998))
end = timeit.timeit()
print("fib_m time: " ,start - end)
