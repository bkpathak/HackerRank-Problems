# https://en.wikipedia.org/wiki/Hamming_weight
# http://ideone.com/vRT7bj

"""
https://wiki.python.org/moin/BitManipulation
Count set bits in python or C
def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)
"""

look_up = [0 for i in range(256)]

def set_look_up():
    for i in range(256):
        for j in range(32):
            if (i >> j & 1):
                look_up[i] += 1

def count_set_bits(arr):
    count = 0
    for n in arr:
        a = n & int('0xFF',16)
        b = (n >> 8) & int('0xFF',16)
        c = (n >> 16) & int('0xFF',16)
        d = (n >> 24) & int('0xFF',16)
        # find the number of bits for each bytes from look_up
        count += look_up[a] + look_up[b] + look_up[c] + look_up[d]

    return count

if __name__ == "__main__":
    arr = [31,51]
    set_look_up()
    print("Number of set bits in array: ",count_set_bits(arr))
