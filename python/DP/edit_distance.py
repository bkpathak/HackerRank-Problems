# http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

# Given two strings str1 and str2 and below operations that can performed
# on str1. Find minimum number of edits (operations) required to convert
# ‘str1′ into ‘str2′.
# Insert
# Remove
# Replace
# All of the above operations are of equal cost.

def edit_distance_recur(str1,str2,m,n):

    # If first string is empty insert all the character from second string
    if m == 0:
        return n
    # If second string is empty remove all the charater from first string
    if n == 0:
        return m

    # If last character is same, get count for remaining characters.
    if str1[m-1] == str2[n-1]:
        return edit_distance_recur(str1,str2,m-1,n-1)

    # If last charster is not same then consider all the operations
    # on the last character of the string
    return 1 + min(edit_distance_recur(str1,str2, m, n-1), # Insert
                    edit_distance_recur(str1,str2,m-1, n), # Remove
                    edit_distance_recur(str1,str2,m-1,n-1) # Replace
                    )

dict_memo = {}
def edit_distance_memo(str1,str2,m,n):
    if (m,n) in dict_memo:
        return dict_memo[(m,n)]

    if m == 0:
        return n

    if n == 0:
        return m

    # If last character is same, get count for remaining characters.
    if str1[m-1] == str2[n-1]:
        return edit_distance_recur(str1,str2,m-1,n-1)

        # If last charster is not same then consider all the operations
        # on the last character of the string
        min_val =  1 + min(edit_distance_recur(str1,str2, m, n-1), # Insert
                edit_distance_recur(str1,str2,m-1, n), # Remove
                edit_distance_recur(str1,str2,m-1,n-1) # Replace
                )
        memo_dict[(m,n)] = min_val

        return min_val

def edit_distance_bottom_up(str1,str2):
    m = len(str1)
    n = len(str2)
    T = [[0] * (n + 1) for i in range (m + 1) ]
    for i in range(m + 1):
        for j in range(n+1):
            # If first string is empty, only option is to insert all
            # the string from second
            if i ==0:
                T[i][j] = j

            # If secind string is epty only options is to remove all
            # the string from second
            if j == 0:
                T[i][j] = i

            # If char at i and char at j are same ignore it and
            # check for remaining characters
            elif str1[i-1] == str2[j-1]:
                T[i][j] = T[i-1][j-1] # Get the minimum till now

            # Find the minumum of insert,remove and replace
            else:
                T[i][j] = 1 + min(T[i][j-1],   # insert
                                  T[i-1][j],   # remove
                                  T[i-1][j-1]) # replace

    return T[m][n]

if __name__ == "__main__":
    str1 = "SUNDAY"
    str2 = "SATURDAY"
    print(edit_distance_recur(str1,str2,len(str1),len(str2)))
    print(edit_distance_memo(str1,str2,len(str1),len(str2)))
    print(edit_distance_bottom_up(str1,str2))
