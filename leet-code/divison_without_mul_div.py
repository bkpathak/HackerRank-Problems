# Integer division without multipication and division
import math
def divide(dividend, divisor):
    flag = 1
    if (dividend < 0) ^ (divisor < 0):
        flag = -1
    dividend = abs(dividend)
    divisor =   abs(divisor)
    result = 0
    while dividend >= divisor:
        shift  = 0
        # shift the divisor tp left(multiply by 2)
        while dividend >= (divisor << shift):
            shift += 1
        # count how many multiples of 2 is required
        result += 1<<(shift - 1)
        # subtract the divisor from the largest shifted divisor less than dividend
        dividend -= divisor << (shift - 1)

    result = flag * result
    # To limit integer overflow(Assuming 4B integer)
    return min(max(result, -2147483648), 2147483647)
print(divide(0,1))
