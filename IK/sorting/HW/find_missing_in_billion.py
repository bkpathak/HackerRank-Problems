"""
http://stackoverflow.com/questions/7153659/find-an-integer-not-among-four-billion-given-ones
"""
from bitarray import bitarray
import numpy as np


def find_missing_number(file_path):
    """
    Create the bit array of size 2^32( 4 billions number are close to
    2^32) and set the bit if the number is present.Pass through the bitarray
    again and return the first bit that is 0.
    """
    bit_array = bit_array(2 ** 32)
    with open("file_path",r) as in in_file:
        for number in in_file:
            bit_array[number] = True

    for index, bit in bit_array:
        if not bit:
            print(index)

def find_missing_number_10mb(file_path):
    """
    """
    nums_in_bin = np.zeros(65536, dtype=np.uint32)
    for N in four_billion_int_array:
        nums_in_bin[N // 65536] += 1
    for bin_num, bin_count in enumerate(nums_in_bin):
        if bin_count < 65536:
            break # we have found an incomplete bin with missing ints (bin_num)

    # Read through the ~4 billion integer list; and count how many ints fall in each of the 2^16 bins and find an incomplete_bin that doesn't have all 65536 numbers. Then you read through the 4 billion integer list again; but this time only notice when integers are in that range; flipping a bit when you find them.
    del nums_in_bin # allow gc to free old 256kB array
    my_bit_array = bitarray(65536) # 32 kB
    my_bit_array.setall(0)
    for N in four_billion_int_array:
        if N // 65536 == bin_num:
            my_bit_array[N % 65536] = 1
    for i, bit in enumerate(my_bit_array):
        if not bit:
            print bin_num*65536 + i
            break
