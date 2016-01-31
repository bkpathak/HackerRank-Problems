# Find the missing number in the list from 1 to N

def find_missing(int_list):
    if len(int_list) == 0:
        return None
    result = 0
    for n in int_list:
        result ^= n
    for n in range(len(int_list) + 1 + 1):
        result ^= n
    return result

data = [[1,2,3,4,6],[1,3,4],[1,2,3,4,5]]
for d in data:
    print(find_missing(d))
