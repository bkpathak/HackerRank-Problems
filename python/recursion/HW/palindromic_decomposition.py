# Complete the function below.

def  palindromicDecomposition( strInput):
    result = []
    part = []
    ans = []
    palindrome_decomp(strInput,0,result,part)
    for i in result:
        ans.append("|".join(i) + '|')
    return ans


def palindrome_decomp(str_input,start,result,part):
    if start == len(str_input):
        result.append(part[:])
    else:
        for i in range(start,len(str_input)):
            if is_palindrome(str_input,start,i):
                part.append(str_input[start:i+1])
                palindrome_decomp(str_input,i+1,result,part)
                part.pop()

def is_palindrome(str_input,start,end):
    while start < end:
        if str_input[start] != str_input[end]:
            return False
        start += 1
        end -= 1
    return True
