# Given the string and dictionary of words, break the string into space
# separated words present int the dictionary.

# Global variable
Dictionary = ['a','e','i','int','inter','interview','kick','kicker','kickstart'
                ,'star','start','view']
memo_map = {}

def create_dictionary():
    # read the lines from Ubuntu built-in english dictionary
    lines = open("/usr/share/dict/american-english").read().splitlines()
    for line in lines:
        Dictionary.append(line)

def break_word_recur(str_in):
    """
    O(N) => 2^N
    """
    if str_in in Dictionary:
        return str_in

    for i in range(len(str_in)):
        prefix = str_in[:i]
        if prefix in Dictionary:
            suffix = break_word_recur(str_in[i:])
            if suffix is not None:
                return prefix + " " + suffix

    return None

def break_word_memo(str_in):
    """
    O(N) => N^2
    """
    if str_in in Dictionary:
        return str_in

    if str_in in memo_map:
        return memo_map[str_in]

    for i in range(len(str_in)):
        prefix = str_in[:i]
        if prefix in Dictionary:
            suffix = break_word_memo(str_in[i:])
            if suffix is not None:
                return prefix + " " + suffix

    memo_map[str_in] = None
    return None

def break_word_bottom_up(str_in):
    """
    O(N) => N^2
    """
    str_len = len(str_in)
    T = [[-1] * len(str_in) for i in range(str_len)]

    for l in range(1, str_len + 1):
        for i in range(str_len - l + 1):
            j = i + l-1
            # Check the string from i to j is in dictionary
            if sub_str in Dictionary:
            sub_str = str_in[i:j+1]
                T[i][j] = i
                continue
            # Find k between i and j such that T[i][k-1] and T[k]T[j] are True
            # i.e if we can divide the string from i to j into word in dictionary

            for k in range(i + 1,j + 1):
                if T[i][k-1] != -1 and T[k][j] != -1:
                    T[i][j] = k
                    break

    # String cannot be break down to words from dictionary
    if T[0][str_len - 1] == -1:
        return None

    # Create the space separated word from T
    result = ""
    i = 0 ; j = str_len - 1
    while i < j:
        k = T[i][j]
        if i == k:
            result += str_in[i:j+1]
            break

        result += str_in[i:k] +  " "
        i = k

    return result


if __name__ == "__main__":

    #create_dictionary()
    print(break_word_bottom_up("interviewkickstart"))
