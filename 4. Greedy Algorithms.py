import random 

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
    for i in range(2, len(list_of_ints)):
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

# PATTERN LEARNED
'''
You don't have to keep track of everything in greedy algorithms as one thing is being tracked by for loop already.

track most fundamental thing
track thing that is an abstraction of the fundamental thing.
track another thing that is an abstraction of the previous abstraction.
this way you can track a lot of things, and all will be based on the fundamental thing.

'''



# GREEDY ALGO 3
def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list) < 2:
        raise IndexError('no enough ints')
    
    product_array = [1] * len(int_list)

    # THIS SOLUTION IS O(2N)
    # product = 1
    # for i in range(len(int_list)):
    #     product_array[i] = product
    #     product *= int_list[i]

    # product = 1
    # for i in range(len(int_list)-1, -1, -1):
    #     product_array[i] *= product
    #     product *= int_list[i]


    # THIS SOLUTION IS O(N)
    prev_product = 1
    next_product = 1

    for i in range(len(int_list)):
        product_array[i] *= prev_product
        prev_product *= int_list[i]
    
        end_index = len(int_list) - (i+1)
        product_array[end_index] *= next_product
        next_product *= int_list[end_index]

    return product_array

# PATTERN LEARNED
'''
For this problem, coming up with a greeday algo was difficult. But we could reach to a greedy algo by starting with a brute force solution, looking for repeat work in that solution, and modifying it to do that work once only

Notice that in this solution we are saving our product, like we do in memoization. But this is not memoization.
'''

# GREEDY ALGO 4
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True

# PATTERN LEARNED
'''
In this algo we are actually not keeping track of anything. We are just incrementing index values and checking if statements.

The thing we need to keep track of is a boolean. We just have to return True or False based on if condition is met or not.
'''



# GREEDY ALGO 5
def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):

    # Shuffle the input in place
    if len(the_list) <= 1:
        return the_list
        
    for index in range(len(the_list)):
        random_index = get_random(index, len(the_list)-1)
        
        the_list[random_index], the_list[index] = the_list[index], the_list[random_index]

    # shuffled_list = []
    # for index in range(len(the_list)):
    #     random_index = get_random(0, len(the_list)-1)
    #     shuffled_list.append(the_list.pop(random_index))


# PATTERN LEARNED
'''
It helps to start by ignoring the in-place requirement, then adapt the approach to work in place.

While shuffling a list, there are two things that can be random.
1. the new order of the items (pick items "serially" from original list and put them in new list "randomly")
2. the picking order of items (pick items "randomly" from original list and put them in new list "serially")
second one will give all the items equal chance of landing at any place in new list.
'''
