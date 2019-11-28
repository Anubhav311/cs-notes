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

    # O(n^2) time and O(1) space
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                return numbers[i]
