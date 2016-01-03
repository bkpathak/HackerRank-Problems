# http://codercareer.blogspot.com/2013/02/no-44-maximal-stolen-values.html
# When the thief reaches ith house he has tow options
# Max sum including the previous element
# Max sum excluding the previous element.
# Then Max sum excluding the current element will be max(incl, excl) and
# max sum including the current element will be excl + current element
# (Note that only excl is considered because elements cannot be adjacent).

def max_value_recur(arr,r):
    if r < 0:
        return 0

    return max(arr[r] + max_value_recur(arr,r-2),max_value_recur(arr,r-1))

memo_dict = {}
def max_value_memo(arr,r):
    # check if present in dict
    if r in memo_dict:
        return memo_dict[r]
    if r < 0:
        return 0

    current_max = max(arr[r] + max_value_memo(arr,r-2),max_value_memo(arr,r-1))
    # put the value in dict
    memo_dict[r] = current_max
    return current_max

# Note inclusive and exclusive means previos adjacent number, not the current
def max_value_bottom_up(arr):
    inclusive = arr[0]
    exclusive = 0
    for i in range(1,len(arr)):
        # Current max excluding i
        new_excl = max(inclusive,exclusive)
        # Current max including i
        inclusive = arr[i] + exclusive
        exclusive = new_excl

    return max(inclusive,exclusive)

if __name__ == "__main__":
    arr = [3,2,7,10]
    print("Max value for array {0} is {1}".format(arr,max_value_recur(arr,len(arr) - 1)))
    print("Max value for array {0} is {1}".format(arr,max_value_memo(arr,len(arr) - 1)))
    print("Max value for array {0} is {1}".format(arr,max_value_bottom_up(arr)))
