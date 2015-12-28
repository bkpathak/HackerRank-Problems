# Classic CS problem.
# Naive : 2^N
# DP = N^2


# Iterative implementation

def lcs_recursion(str1, str2):
    """
    This is a correct solution but it's very time consuming.
    For example, if the two strings have no matching characters,
    so the last line always gets executed, the the time bounds are
    binomial coefficients, which (if m=n) are close to 2^n.
    """
    if len(str1) == 0 or len(str2) == 0:
        return ""
    if str1[0] == str2[0]:
        return str1[0] + lcs_recursion(str1[1:], str2[1:])
    else:
        r1 = lcs_recursion(str1,str2[1:])
        r2 = lcs_recursion(str1[1:],str2)
        r = r1 if len(r1) > len(r2) else r2
        return r

def lcs_memoization(str1,str2):
    # allocate storage for L
    len1 = len(str1)
    len2 = len(str2)
    L = [[-1 for i in range(len1)] for j in range(len2)]

    return lcs_memo_util(str1,str2,0,0,L)

def lcs_memo_util(str1,str2,i,j,L):
    if i >= len(str1) or j >= len(str2):
        return 0
    if L[i][j] < 0:
        if str1[i] == "" or str2[j] == "":
            L[i][j] = 0
        elif str1[i] == str2[j]:
            L[i][j] = 1 + lcs_memo_util(str1,str2,i+1,j+1,L)
        else:
            L[i][j] = max(lcs_memo_util(str1,str2,i,j+1,L),lcs_memo_util(str1,str2,i+1,j,L))
    return L[i][j]

def lcs_bottom_up(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    # initialize the array
    L = [[None] * (len2+1) for i in range(len1+1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j]  = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    sub_seq = ""
    i = 1
    j = 1
    while i < len1 and j < len2:
        if str1[i-1] == str2[j-1]:
            sub_seq =  sub_seq + str1[i - 1]
            i += 1
            j += 1

        elif L[(i - 1)+1][j - 1] <= L[j - 1 ][(i - 1)+1]:
            i += 1
        else:
            j += 1
    return sub_seq


if __name__ == "__main__":
    str1 = "ABCDGH"
    str2 = "AEDFHR"

    print("Max Length: ",lcs_recursion(str1,str2))
    print("Max Length: ",lcs_memoization(str1,str2))
    print("Max Length: ", lcs_bottom_up(str1,str2))
