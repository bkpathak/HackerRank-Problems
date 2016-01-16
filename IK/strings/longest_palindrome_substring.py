# http://stevekrenzel.com/articles/longest-palnidrome
# http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/


def longest_palindrome(string):
    if len(string) <= 1:
        return string
    longest = string[0]

    for i in range(len(string)):
        # Get longest palindrome with center i
        temp = find_palindrome(string,i,i)
        if len(temp) > len(longest):
            longest = temp

        # Get the palindrome with center i, i+1
        temp = find_palindrome(string, i, i+1)
        if len(temp) > len(longest):
            longest = temp

    return longest

def find_palindrome(string,start,end):
    while (start >= 0 and end < len(string) and string[start] == string[end]):
        start -= 1
        end += 1
    return string[start+1:end]

if __name__ == "__main__":
    input = "CARRACECARCAR"
    print(longest_palindrome(input))
