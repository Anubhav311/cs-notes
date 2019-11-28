# Adapted binary search
def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        # Guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) / 2)

        # If guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # Go right
            floor_index = guess_index
        else:
            # Go left
            ceiling_index = guess_index

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index

# PATTERN LEARNED
'''
Binary search doesn't only work on sorted lists. It can also work with partially sorted lists.
'''



# BINARY SEARCH, PIGEONHOLE PROBLEM
def find_repeat(numbers):

    # Find a number that appears more than once

    # # O(n) time and O(n) space
    # integers_set = set()
    
    # for num in numbers:
    #     if num in integers_set:
    #         return num
    #     else:
    #         integers_set.add(num)
    
    # return Exception('no duplicates')

    # # O(n^2) time and O(1) space
    # for i in range(len(numbers)):
    #     for j in range(i+1, len(numbers)):
    #         if numbers[i] == numbers[j]:
    #             return numbers[i]

    # # O(n log n) time and O(1) space. But here we are modifying the input.
    # numbers.sort()
    # for i in range(len(numbers)):
    #     if numbers[i] == numbers[i+1]:
    #         return numbers[i]

    # #O(n log n) time and O(1) space. Without modifying the input.
    # floor = 1
    # ceiling = len(numbers) - 1

    # while floor < ceiling:
    #     midpoint = floor + ((ceiling - floor) / 2)
    #     lower_range_floor, lower_range_ceiling = floor, midpoint
    #     upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

    #     items_in_lower_range = 0
    #     for item in numbers:
    #         if item >= lower_range_floor and item <= lower_range_ceiling:
    #             items_in_lower_range += 1

    #     distinct_possible_integers_in_lower_range = (
    #         lower_range_ceiling
    #         - lower_range_floor
    #         + 1
    #     )
    #     if items_in_lower_range > distinct_possible_integers_in_lower_range:
    #         floor, ceiling = lower_range_floor, lower_range_ceiling
    #     else:
    #         floor, ceiling = upper_range_floor, upper_range_ceiling

    # return floor

    # O(3n) time and O(1) space. Without modifying the input.
    n = len(numbers) - 1

    position_in_cycle = n + 1
    for _ in range(n):
        position_in_cycle = numbers[position_in_cycle - 1]

    remembered_position_in_cycle = position_in_cycle
    current_position_in_cycle = numbers[position_in_cycle - 1]
    cycle_step_count = 1

    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = numbers[current_position_in_cycle - 1]
        cycle_step_count += 1

    pointer_start = n + 1
    pointer_ahead = n + 1
    for _ in range(cycle_step_count):
        pointer_ahead = numbers[pointer_ahead - 1]

    while pointer_start != pointer_ahead:
        pointer_start = numbers[pointer_start - 1]
        pointer_ahead = numbers[pointer_ahead - 1]

    return pointer_start

# PATTERN LEARNED
'''
We solved this problem by thinking about a target runtime, and then started optimizing our solution for that runtime.

Starting with a target runtime and working backward from there can be a powerful strategy for all kinds of coding interview questions.

This problem also shows how important hints can be. A simple hint can give you an insight for improving the solution. So when you get a hint, drop everything and listen carefully.
'''



# COUNTING SEARCH
def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        while range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores

# PATTERN LEARNED
'''
In this problem, we are using greedy algo and counting algo for searching something.
That means we greedy/counting algo can also work like a searching algorithm.

Think about other algorithms that can work together to solve a problem.
'''