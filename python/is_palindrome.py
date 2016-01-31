"""
Check if string is plaindrome or not.
"""
import re
def is_palindrome(string):
    #strip the non alphanumeric character
    pattern = re.compile('[^a-zA-Z0-9]')
    clean_string = pattern.sub('',string).lower()
    return is_palindrome_util(clean_string,0,len(clean_string)-1)

def is_palindrome_util(string,l,r):
    if l == r or l > r:
        return True
    if string[l] == string[r] and is_palindrome_util(string,l+1,r-1):
        return True
    else:
        return False

data = ['raceCar',"Not palindrome",'Sore was I ere I saw Eros.',
'A man, a plan, a canal -- Panama','Never a foot too far, even.']
for d in data:
    print(is_palindrome(d))
