# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# Do pattern matching using KMP algorithm
# Runtime complexity - O(m + n) where m is length of text and n is length of pattern

def compute_suffix_array(pattern):
    """
    Compute temporary array to maintain size of suffix which is same as prefix
    Time/space complexity is O(size of pattern)
    """
    len_pattern = len(pattern)
    temp_array = [0] * len_pattern
    index  = 0
    i = 1
    while i < len_pattern:
        if pattern[i] == pattern[index]:
            temp_array[i] = index + 1
            index += 1
        else:
            if index != 0:
                index  = temp_array[index -1]
                i += 1
            else:
                temp_array[i] = 0
                i += 1

    return temp_array

def kmp_search(text, pattern):
    suffix_array = compute_suffix_array(pattern)
    i ,j  = 0,0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = suffix_array[j - 1]
            else:
                i += 1

    if j == len(pattern):
        return True
    else:
        return False

if __name__ == "__main__":
    str = "asdfxhijasdfghudkasdfgh"
    pattern = "asdfgh"

    if kmp_search(str,pattern):
        print("{0} is present in {1}".format(pattern,str))
    else:
        print("Pattern is not present.")
