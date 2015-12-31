# Implements the recursive Catalan number computation

def find_nth_catalan(n):
    if n == 0:
        return 1
    else:
        result = 0
        for i in range(n):
            result += find_nth_catalan(i) * find_nth_catalan(n- i - 1)
        return result

if __name__ == "__main__":
    print(find_nth_catalan(10))
