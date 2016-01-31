"""
Find the total number of sub_sequence of the string.
"""

def sub_sequence(str_L, str_S,l,s):
    if s == len(str_S):
        return 1
    if l == len(str_L):
        return 0
    result = 0
    if(str_L[l] == str_S[s]):
        result += sub_sequence(str_L, str_S,l+1,s+1)
    result += sub_sequence(str_L,str_S,l + 1,s)
    return result

print(sub_sequence("ababc","abc",0,0))
