# http://www.geeksforgeeks.org/check-whether-a-given-string-is-an-interleaving-
# of-two-other-given-strings-set-2/

def is_interleave(str_a,str_b,str_c,a,b,c):

    # If we reach the end of all three string
    #if a == len(str_a) and b == len(str_b) and c == len(str_c):
    #        return True

    # If we reach the end of string C but not of either A or B
    #if c == len(str_c) and (a < len(str_a) or b < len(str_b)):
    #    return False

    if a == len(str_a):
        return str_b[b:] == str_c[c:]
    if b == len(str_b):
        return str_a[a:] == str_c[c:]

    # Check recursively for all the characters
    if ((str_a[a] == str_c[c] and is_interleave(str_a,str_b,str_c,a+1,b,c+1))
            or (str_b[b] == str_c[c] and is_interleave(str_a,str_b,str_c,a,b+1,c+1))):
        return True

    return False

# If need to check for mutiple str_c make dict local
dict_memo = {}
def is_interleave_memo(str_a,str_b,str_c,a,b,c):
    # Check if already computed
    if (a,b) in dict_memo:
        return dict_memo[(a,b)]
    if a == len(str_a):
        return str_b[b:] == str_c[c:]
    if b == len(str_b):
        return str_a[a:] == str_c[c:]

    if ((str_a[a] == str_c[c] and is_interleave_memo(str_a,str_b,str_c,a + 1,b,c+1)) or
        (str_b[b] == str_c[c] and is_interleave_memo(str_a,str_b,str_c,a,b+1,c+1))):
        dict_memo[(a,b)] = True
        return True

    dict_memo[(a,b)] = False
    return False


def is_interleave_bottom_up(str_a,str_b,str_c):
    a = len(str_a)
    b = len(str_b)

    if (a + b) != len(str_c):
        return False

    # Temp array
    T = [[False] * (b + 1) for i in range(a + 1)]
    # For all the characters of A
    for i in range(a + 1):
        # For all the characters of B
        for j in range(b+1):
            # empty string has empty string is interleaving
            if i == 0 and j == 0:
                T[i][j] = True

            # If A is empty ; check B and C
            elif i == 0 and str_b[j-1] == str_c[j-1]:
                T[i][j] = T[i][j-1]

            # If B is empty ; check B and C
            elif j == 0 and str_a[i-1] == str_c[i-1]:
                T[i][j] = T[i-1][j]

            # current char of C matches with A but not with B
            elif str_a[i-1] == str_c[i+j-1] and str_b[j-1] != str_c[i+j-1]:
                T[i][j] = T[i-1][j]

            # current cchar of C matches with B but not with A
            elif str_a[i-1] != str_c[i+j-1] and str_b[j-1] != str_c[i+j-1]:
                T[i][j] = T[i][j-1]

            # Current char of C matches with both A and B
            elif str_a[i-1] == str_c[i+j-1] and str_b == str_c[i+j-1]:
                T[i][j] = T[i-1][j] or T[i][j-1]
    return T[a][b]

if __name__ == "__main__":
    a = "XY"
    b = "YZ"
    c = "WZXY"

    if is_interleave_bottom_up(a,b,c):
        print("{0} is interleave of {1} and {2}.".format(c,a,b))
    else:
        print("{0} is not interleave of {1} and {2}.".format(c,a,b))
