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



# GREEDY ALGO 2
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # We could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Walk through items, starting at index 2
    for i in xrange(2, len(list_of_ints)):
        current = list_of_ints[i]

        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        # Do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3

