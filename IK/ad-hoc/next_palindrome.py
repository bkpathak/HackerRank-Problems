# Given the number N find the next smallest palindrome
# number greater than this number.
# input => 23545
# output => 23632

import math
def next_palindrome(number):
    length = len(str(number))
    is_odd = (length % 2) != 0
    left_half = str(number)[:length//2]
    middle_num = str(number)[(length-1)//2]

    # if number is of odd digit
    if is_odd:
        incr = pow(10,length // 2)
        new_num = int(left_half + middle_num + left_half[::-1])
    else:
        incr = 1.1 * pow(10, length // 2)
        new_num  = int(left_half + left_half[::-1])
    if new_num > number:
        return new_num
    if middle_num != '9':
        return int(new_num + incr) # check why addition is giving float
    else:
        return next_palindrome(round_up(number))

def round_up(number):
    length = len(str(number))
    incr = pow(10,((length // 2) + 1))
    return ((number // incr) +1) * incr

if __name__ == "__main__":
    num = [23545,99,1234,6789876,8998]
    print("Original Number.")
    print(num)
    for n in num:
        print(next_palindrome(n), end = ",")

    print()
