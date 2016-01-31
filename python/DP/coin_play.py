# Consider a row of n coins of values v1 . . . vn, where n is even.
# We play a game against an opponent by alternating turns. In each turn,
# a player selects either the first or last coin from the row, removes it
# from the row permanently, and receives the value of the coin. Determine the
# maximum possible amount of money we can definitely win if we move first.
# Note: The opponent is as clever as the user.
# http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/

def find_max_val_recur(coins,l,r):
    if l + 1  == r:
        return max(coins[l],coins[r])
    if l == r:
        return coins[i]

    left_choose = coins[l] + min(find_max_val_recur(coins,l+1,r - 1),find_max_val_recur(coins,l+2,r))
    right_choose = coins[r] + min(find_max_val_recur(coins,l + 1,r-1),find_max_val_recur(coins,l,r-2))
    return max(left_choose,right_choose)

coin_map = {}
def find_max_val_memo(coins,l,r):
    if l + 1 == r:
        return max(coins[l],coins[r])
    if l == r:
        return coins[i]

    if (l,r) in coin_map:
        return coin_map[(l,r)]

    left_choose = coins[l] + min(find_max_val_memo(coins,l+1,r - 1),find_max_val_memo(coins,l+2,r))
    right_choose = coins[r] + min(find_max_val_memo(coins,l + 1,r-1),find_max_val_memo(coins,l,r-2))
    max_val = max(left_choose,right_choose)
    coin_map[(l,r)] = max_val
    return max_val

def find_max_val_bottom_up(coins):
    coins_len = len(coins)
    table = [[0] * coins_len for i in range(coins_len + 1)]
    for gap in range(coins_len):
        i = 0
        for j in range(gap,coins_len):
            # Here x is value of F(i+2, j), y is F(i+1, j-1) and
            # z is F(i, j-2) in above recursive formula
            x = table[i+2][j] if (i+2) <= j else 0
            y = table[i+1][j-1] if (i+1) <= (j-1) else 0
            z = table[i][j-2] if i <= (j-2) else 0
            table[i][j] = max(coins[i] + min(x,y),coins[j] + min(y,z))
            i += 1
    return table[0][coins_len - 1]

if __name__=="__main__":
    coins = [8,15,3,7]
    print(find_max_val_bottom_up(coins))
