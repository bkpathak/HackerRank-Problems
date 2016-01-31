"""
Conversion of atoi in python
"""

def atoi(string):
    if len(string) == 0 or str == None:
        return 0
    # Trim whitespace
    string = string.strip()
    sign_flag = False
    index = 0
    if string[index] in "+-":
        sign_flag = True
        index += 1
    res = 0
    string_len = len(string)
    while (string_len > index and ord(string[index]) >= ord('0') and ord(string[index]) <= ord('9')):
        res = res * 10 + ord(string[index]) - ord('0')
        index += 1

    if sign_flag and string[0] == "-":
        res = -1 * res

    ### Assuming 32 bit integer(Python 3 supports 64 bit integer)
    if res > 2147483647:
        return "overflow"
    if res < -2147483648:
        return "overflow"

    return res

test_data = ["1234","  -2345","123x34","x3345",'12234567654345654']

for d in test_data:
    print(atoi(d))
