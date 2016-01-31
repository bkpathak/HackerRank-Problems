# https://www.google.com/webhp?sourceid=chrome-
# instant&ion=1&espv=2&ie=UTF-8#q=dp%20coin%20change

def coin_change_recur(coins,n,change_sum):
    # If sum is 0 there exists a solution with no coins
    if change_sum == 0:
        return 1
    # if sum is less then 0 no solution exists
    if change_sum < 0:
        return 0
    # if there is no coins left and sum is not 0 then no solution
    # exists
    if n <= 0 and change_sum > 0:
        return 0

    # counts the solution including the coins[n-1] and excluding the coins[n-1]
    return (coin_change_recur(coins,n-1,change_sum) +
                coin_change_recur(coins,n,change_sum - coins[n-1]))

# To hold the results that has been already computed
memo_dict = {}
def coin_change_memo(coins,n,change_sum):
    # Check if we have already computed for the current change_sum
    if change_sum in memo_dict:
        return memo_dict[change_sum]

    # If sum is 0 there exists a solution with no coins
    if change_sum == 0:
        return 1
    # if sum is less then 0 no solution exists
    if change_sum < 0:
        return 0
    # if thhere are no coins left and sum is not 0 then no solution exists
    if n <= 0 and change_sum > 0:
        return 0

    # count the solution inclusding coins[n-1] and excluding coins[n-1]
    count = (coin_change_memo(coins,n-1,change_sum) +
                coin_change_memo(coins,n,change_sum - coins[n-1]))

    #memo_dict[change_sum] = count
    return count

def coin_change_bottom_up(coins,change_sum):
    coins_len = len(coins)
    T = [[0] * (coins_len) for i in range(change_sum + 1)]

    # Initialize the base case : getting sum 0
    for i in range(coins_len):
        T[0][i] = 1

    for i in range(1, change_sum + 1):
        for j in range(coins_len):
            # Solutions including coins[j]
            x = T[i - coins[j]][j] if i >= coins[j] else 0
            # Solutions excluding coins[j]
            y = T[i][j-1] if j >= 1 else 0
            # total count
            T[i][j] = x + y
    return T[change_sum][coins_len - 1]

if __name__ == "__main__":
    coins = [1,2,3]
    print("Number of ways to make change: ", coin_change_recur(coins,len(coins),4))
    print("Number of ways to make change: ", coin_change_memo(coins,len(coins),4))
    print("Number of ways to make change: ", coin_change_bottom_up(coins,4))
