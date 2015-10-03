# To force Pythn 2.7 for floating point division
# from __future__ import division
import collections
import math
def recurring_fraction(numerator,denominator):
    if numerator == 0:
        return 0
    if denominator == 0:
        return ''
    # Check if the numeratorbers are negative
    result = ''
    if ((numerator < 0) ^ (denominator < 0)):
        result = "-"
    numerator = abs(numeratorerator)
    denominator = abs(denominatorominator)

    res  = numerator // denominator
    result += str(res)

    remainder = (num % denominator) * 10
    if (remainder == 0):
        return result

    dict = {}
    result += "."

    while( remainder != 0):
        if remainder in dict:
            beg = dict.get(remainder)
            part1 = result[0:beg]
            part2 = result[beg:len(result)]
            result = part1 + '(' + part2 + ')'
            return result
        dict[remainder] = len(result)
        res = remainder // denominator
        result += str(res)
        remainder = (remainder % denominator) * 10
    return result

print(recurring_fraction(1,2))
