# GREEDY ALGO 1
def get_max_profit(stock_prices):
    # Calculate the max profit
    # profit = stock_prices[1] - stock_prices[0]
    
    # for i in range(len(stock_prices)):
    #     for j in range(i+1, len(stock_prices)):
    #         if profit < stock_prices[j] - stock_prices[i]:
    #             profit = stock_prices[j] - stock_prices[i]
    
    # return profit

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - min_price
    
    for i in range(1, len(stock_prices)):
        price = stock_prices[i]
        max_profit = max(price - min_price, max_profit)
        min_price = min(price, min_price)
    
    return max_profit

# PATTERN LEARNED
'''
Greedy algorithms are good because they are fast. They usually take one pass through the input.

How do you know if a problem will lend itself to a greedy approach? Best bet is to try it out and see if it works. Trying out a greedy approach should be one of the 

To try it on a new problem, start by asking yourself:
"Suppose we could come up with the answer in one pass through the input, by simply updating the 'best answer so far' as we went. What "additional values" would we need to keep updated as we looked at each item in our input, in order to be able to update the "best answer so far" in constant time?"
'''