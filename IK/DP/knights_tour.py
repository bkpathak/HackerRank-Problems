# Given a phone keypad as shown below:

# 1 2 3
# 4 5 6
# 7 8 9
#   0
# How many different 10-digit numbers can be formed starting from 1?
# The constraint is that the movement from 1 digit to the next is similar
# to the movement of the Knight in a chess game.
# For eg. if we are at 1 then the next digit can be either 6 or 8 if we are at 6
# then the next digit can be 1, 7 or 0.

# Repetition of digits are allowed - 1616161616 is a valid number.

knight_move = {
    1 : [8,6],
    2 : [7,9],
    3 : [4,8],
    4 : [0,9],
    5 : None,
    6 : [0,7],
    7 : [2,6],
    8 : [1,3],
    9 : [2,4],
    0 : [4,6]
}

def find_10_digit_num_count(start_num,count):
    if count == 1:
        return 1
    if start_num == 5:
        return 0
    # find the knight next position
    next_move = knight_move[start_num]
    return find_10_digit_num_count(next_move[0],count - 1) + find_10_digit_num_count(next_move[1],count - 1)

memo_dict = {}
def find_10_digit_num_count_memo(start_num,count):
    if count == 1:
        return 1
    if start_num == 5:
        return 0
    # check if already computed
    if (start_num,count) in memo_dict:
        return memo_dict[(start_num,count)]

    # find the next position
    next_move = knight_move[start_num]
    first_move = find_10_digit_num_count_memo(next_move[0], count - 1)
    second_move = find_10_digit_num_count_memo(next_move[1], count - 1)
    memo_dict[(start_num,count)] = first_move + second_move
    return (first_move+second_move)

if __name__ == "__main__":

    print(find_10_digit_num_count(1,100))
    print(find_10_digit_num_count_memo(1,100))
