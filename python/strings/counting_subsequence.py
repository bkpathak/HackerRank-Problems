"""
Counts the number of sub_sequence in the string.
Example:
string = "ababc" sub_str = "abc"
Number of sub_seq: 3
"""

def find_sub_seq_count(string,sub_str):
    if sub_str == "":
        return 1
    if string == "":
        return 0

    result = 0
    if string[0] == sub_str[0]:
        result += find_sub_seq_count(string[1:],sub_str[1:])
    result += find_sub_seq_count(string[1:],sub_str)
    return result

print(find_sub_seq_count("ababc","abc"))
