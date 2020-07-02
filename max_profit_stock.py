def find_max_profit(prices):
    lowest = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):

        current_profit = prices[i] - lowest

        if current_profit > max_profit:
            max_profit = current_profit
            # print("sell price ", prices[i])
            # print("buy price ", lowest)

        if prices[i] < lowest:
            lowest = prices[i]

    return max_profit


stock_prices = [
    [7, 1, 5, 3, 4, 6, 2],
    [7, 7, 7],
    [7, 6, 5, 4],
    [1, 2, 3, 4, 5]]

for stock_price in stock_prices:
    print("\n")
    max_profit = find_max_profit(stock_price)
    print("max_profit ", max_profit)
