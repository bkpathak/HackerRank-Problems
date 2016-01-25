# http://stevekrenzel.com/articles/longest-palnidrome
# http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

def longets_palindrome_recur(string,left,right):
    # Base case: if length is 1 return 1
    if left == right:
        return 1
    # Base case: if length is 2 and both character are same return 2
    if string[left] == string[right] and left + 1 == right:
        return 2

    if string[left] == string[right]:
        return longets_palindrome_recur(string, left + 1, right - 1 ) + 2

    return max(longets_palindrome_recur(string,left + 1,right),
        longets_palindrome_recur(string,left, right-1))

memo_dict = {}
def longest_palindrome_memo(string,left,right):
    # Check if we have already computed for the sequence (left,right)
    if (left,right) in memo_dict:
        return memo_dict[(left,right)]

    # Base case: if length is 1 return 1
    if left == right:
        return 1
    # Base case : if length is 2 and both character are same return 2
    if string[left] == string[right] and left + 1 == right:
        return  longest_palindrome_memo(string, left + 1, right - 1) + 2


    result = max(longets_palindrome_recur(string,left + 1,right),
                    longets_palindrome_recur(string,left, right-1))
    memo_dict[(left,right)] = result

    return result


def longest_palindrome_bottom_up(string):
    n = len(string)

    # Create the temp table to store the results of subproblem
    T = [[0] * n for i in range(n)]

    # String of length 1 are palindrome of length 1
    for i in range(n):
        T[i][i] = 1

    for c in range(2, n + 1):
        for i in range(n-c + 1):
            j = i + c - 1
            if string[i] == string[j] and c == 2:
                T[i][j] = 2
            elif string[i] == string[j]:
                T[i][j] = T[i+1][j-1] + 2
            else:
                T[i][j] = max(T[i][j-1],T[i + 1][j])
    return T[0][n-1]

if __name__ == "__main__":
    input_str = "CARRACECARCAR"
    #print(longets_palindrome_recur(input_str,0,len(input_str) - 1))
    #print(longest_palindrome_memo(input_str,0,len(input_str) - 1))
    print(longest_palindrome_bottom_up(input_str))
