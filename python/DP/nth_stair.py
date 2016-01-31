# http://www.geeksforgeeks.org/count-ways-reach-nth-stair/
# This problem is simpl extension of Fibonacci Number

# Case 1 when person can take 1 or 2 steps

def fibonacci_number(n):
    if n <= 1:
        return n
    return fibonacci_number(n-1) + fibonacci_number(n-2)

def count_ways(s):
    # ways(1) = fib(2) = 1
    # ways(2) = fib(3) = 2
    # ways(3) = fib(4) = 3
    return fibonacci_number(s+1)

# generalized version
# if person can take m steps (1,2,3.....m-1,m)

def count_ways_util(n,m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i <= m and i <= n:
        res += count_ways_util(n-i,m)
        i += 1
    return res

def count_ways_generalize(s,m):
    return count_ways_util(s+1,m)

if __name__ == "__main__":
    print("Number of ways: ",count_ways_generalize(4,2))
