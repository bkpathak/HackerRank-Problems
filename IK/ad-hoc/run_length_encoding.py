"""
Generate all Numeronyms for any given stirng (char array)
Eg.
input => "nailed"
output => "n4d","na3d","nai2d","n3ed","n2led","na2ed"
"""

def run_len_encoding(in_string):
    str_len = len(in_string)-1
    right = str_len - 1
    for i in range(1,str_len):
        rle_l = str_len - i
        if rle_l > 1:
            print(in_string[:i] + str(rle_l)+in_string[-1])
        rle_r = str_len - i -1
        if rle_r > 1:
            print(in_string[0] + str(rle_r) + in_string[right:] )

        rle_mid = right - i - 1
        if rle_mid > 1:
            print(in_string[:i + 1] + str(rle_mid) + in_string[right:])

        right -= 1

if __name__ == "__main__":
    run_len_encoding("NAILED")
