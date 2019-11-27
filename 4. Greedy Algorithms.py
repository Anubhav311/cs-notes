# GREEDY ALGO 1
def get_max_profit(stock_prices):
    # Calculate the max profit
    profit = stock_prices[1] - stock_prices[0]
    
    for i in range(len(stock_prices)):
        for j in range(i+1, len(stock_prices)):
            if profit < stock_prices[j] - stock_prices[i]:
                profit = stock_prices[j] - stock_prices[i]
    
    return profit
