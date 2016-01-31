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

#  Below shows how the DP table is filled
#       0   1   2  3    4   5    6  7   8    9        Digit in the keypad
#   1   1   1   1   1   1   0   1   1   1    1        Count for 1 digit
#   2   2   2   2   2   2   0   2   2   2    2        Count for 2 digit
#   3   4   4   4   4   4   0   4   4   4    4        Count for 3 digit
#   4   8   8   8   8   8   0   8   8   8    8
#   .   . . . . . . . . . .
#   10 512 512 512 512 512  0 512 512 512 512         Count for 10 digit
# The table id filled by adding the the value from the posotion which leads to
# the current position
# e.g Count of numbers form of length 3 dtarting at 1 is given by sum of counts
# of length 2 at position 6 and 8
# If we look closely the answer is just 2 ** (digit_count -1) , since in each
# number can be reached from 2 other number

def find_10_digit_num_count_memo_bottom_up(start_num,count):
    # Auxillary array to hold the result
    S = [[0] * 10 for i in range(count)]

    # Initialize the base case
    for i in range(10):
        S[0][i] = 1
    # Set 0 for 5
    S[0][5] = 0


    for i in range(1,count):
        for j in range(10):
            previous_pos = knight_move[j]
            if previous_pos is not None:
                S[i][j] = S[i-1][previous_pos[0]] + S[i-1][previous_pos[1]]
            else:
                S[i][j] = 0

    return S[count-1][start_num]

if __name__ == "__main__":

    print(find_10_digit_num_count(1,10))
    print(find_10_digit_num_count_memo(1,10))
    print(find_10_digit_num_count_memo_bottom_up(1,10))
