# Implement the catalan number
# https://en.wikipedia.org/wiki/Catalan_number
# Recursive catalan definition
# C0 = 1
# C1 = 1
# C2 = C0C1 + C1C0
# C3 = C0C2 + C1C1 + C2C0
# C4 = C0C3 + C1C2 + C2C1 + C3C0

# Dictionary to remember previous calculation
memo = {}

def find_nth_catalan(n):
    if n == 0:
        return 1
    else:
        result = 0
        for i in range(n):
            result += find_nth_catalan(i) * find_nth_catalan(n-i - 1)
        return result

def find_nth_catalan_memo(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    else:
        result = 0
        for i in range(n):
            result += find_nth_catalan_memo(i) * find_nth_catalan_memo(n-i - 1)
        memo[n] = result
        return result

def find_nth_catalan_bottom_up(n):
    # Array to hold the result
    C = [0] * (n + 1)
    # Set initial value
    C[0],C[1] = 1,1
    for i in range(2,n + 1):
        for j in range(i):
            C[i] += C[j] * C[i - j -1]

    return C[n]

if __name__  == "__main__":
    print(find_nth_catalan_memo(10))
    print(find_nth_catalan_bottom_up(10))
