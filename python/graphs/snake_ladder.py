"""
The snake ladder board game is represented as one-dimensional array
where value in the array are the destination id cell for the snakes (lower
numbers) and ladders higher number.
"""

board = [1,15,3,4,7,6,7,8,27,10,11,12,13,14,15,16,4,29,19,21,22,23,16,
            35,26,27,28,29,30,31,30,33,12,35,36]

def find_min_throws(position,count, min_count):
    if position == 36:
        if count[0] < min_count[0]:
            min_count[0] = count[0]
        return

    for dice_top in [1,2,3,4,5,6]:
        next_position = dice_top + position
        if next_position > 36:
            next_postion = position + (36-position) - (dice_top - (36 -position))
        else:
            next_position = next_position
        actual_position = board[next_position]
        count[0] += 1
        find_min_throws(actual_position,count,min_count)

def play_game():
    min_count = [0]
    count = [0]
    find_min_throws(1,count,min_count)
    print(min_count)

play_game()
