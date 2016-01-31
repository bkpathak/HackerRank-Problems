# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
# The algorithm is implementation of wikipedia article

prime  = 101
import math

def pattern_search(text,pattern):
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m)
    text_hash = create_hash(text, m)
    for i in range(1, n-m + 2):
        if pattern_hash == text_hash and check_equal(text,i-1,i + m - 2, pattern,0,m-1):
            return i - 1
        if (i < n - m +1):
            text_hash = re_calculate_hash(text,i -1, i + m - 1, text_hash , m)
    return -1

def re_calculate_hash(text, old_index, new_index,old_hash, pattern_len):
    new_hash = (old_hash - ord(text[old_index])) / prime
    new_hash += ord(text[new_index]) * math.pow(prime, pattern_len - 1)
    return new_hash

def create_hash(text,len):
    hash_val = 0
    for i in range(len):
        hash_val += ord(text[i]) * math.pow(prime,i)
    return hash_val

def check_equal(str1,start1,end1,str2,start2,end2):
    if (end1 - start1) != (end2 - start2):
        return False

    while start1 <= end1 and start2 <= end2:
        if str1[start1] != str2[start2]:
            return False

        start1 += 1
        start2 += 2

    return True

if __name__ == "__main__":
    print(pattern_search("Programming is fun","is"))
