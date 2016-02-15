# Find the max profit that can be made from buying and selling the stocks

def max_profit(stock_val):
    max_profit = 0
    min_stock_val = stock_val[0]

    for v in stock_val[1:]:
        profit = v - min_stock_val
        if profit > max_profit:
            max_profit = profit
        if v < min_stock_val:
            min_stock_val = v

    return max_profit

if __name__ == "__main__":
    arr = [10,7,5,8,10,11]
    print("Max profit is:", max_profit(arr))
