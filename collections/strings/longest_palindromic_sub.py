def palin_sub(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    longest_seq = string[0]
    for i in range(len(string)):
        # get palindrome with odd length
        tmp = is_palindrome(string,i,i)
        if len(tmp)  > len(longest_seq):
            longest_seq = tmp
        # get palindrome with even length
        tmp = is_palindrome(string,i,i+1)
        if len(tmp) > len(longest_seq):
            longest_seq = tmp

    return longest_seq if len(longest_seq) > 1 else ""
def is_palindrome(string,beg,end):
    while beg >= 0 and end < len(string) and string[beg] == string[end]:
        beg -= 1
        end += 1
    return string[beg + 1:end]

print(palin_sub("ASDFGHJK"))
