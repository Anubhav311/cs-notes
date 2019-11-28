# SOLUTION TO ARRAY 1
def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)
    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))
            
    return merged_meetings


# PATTERN LEARNED
'''
How to check if something is overlapping some other thing in terms of time: 
Ending of the first thing will happen after starting of the second thing.
This pattern can be used in other areas where we need to merge overlapping things.

In this case, most fundamental unit is the tuple. So there's no need to breakdown the problem to individual values in the tuples. You only need to break them down to tuple level (not below that). Tuples fundamental because they will give you predictive abilities with respect to the problem. So the lesson is that we shouldn't always try to breakdown the problem to all the way down. Stop at the fundamental level. Don't go below that.

This problem is using greedy approach and sorting. So it's a lesson that these two algos can work together.
'''



# SOLUTION TO ARRAY 2
def reverse(list_of_chars):

    # Reverse the input list of chars in place
    length = len(list_of_chars)
    
    if len(list_of_chars) < 2:
        return list_of_chars
        
    for i in range((len(list_of_chars)/2)):
        list_of_chars[i], list_of_chars[length-(i+1)] = list_of_chars[length-(i+1)], list_of_chars[i]

    return list_of_chars

# PATTERN LEARNED
'''
How to track begining and end of a list in single iteration.
It is called a "two pointer" technique
'''



# REVERSE WORDS
def reverse_words(message):
    # Reverse the input list of chars in place
    length = len(message)
    emptySpace = []
    length = len(message)
    
    if length < 1:
        return message
        
    # reversing the whole string 
    for i in range(int(length/2)):
        message[i], message[length-(i+1)] = message[length-(i+1)], message[i]
        if message[i] == ' ':
            emptySpace.append(i)
        if message[length-(i+1)] == ' ':
            emptySpace.append(length-(i+1))
        
    sortedEmptySpaces = sorted(emptySpace)
    sortedEmptySpaces.append(len(message))
    
    #reversing the words in place
    wordStart = 0
    for i in sortedEmptySpaces:
        wordEnd = i-1
        
        while wordStart < wordEnd:
            message[wordStart], message[wordEnd] = message[wordEnd], message[wordStart]
            wordStart += 1
            wordEnd -= 1
            
        wordStart = i+1

    return message


# PATTERN LEARNED
'''
reversing words is a sub-problem of reversing string.
solving a simpler problem can give you insight into solving more complex problem.
'''



# MERGE SORTED ARRAYS
def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    # edge cases
    # 1. arrays with different lengths
    # 2. some of the numbers can be present in both of the arrays
    # 3. can one or both arrays be empty

    mergedArray = [0] * (len(my_list) + len(alices_list))

    for i in range(len(mergedArray)):
        # print(indexA, indexB, i)
        if len(my_list) == 0:
            mergedArray[i] = alices_list.pop(0)
        elif len(alices_list) == 0:
            mergedArray[i] = my_list.pop(0)
        else:
            if my_list[0] <= alices_list[0]:
                mergedArray[i] = my_list.pop(0)
            else:
                mergedArray[i] = alices_list.pop(0)
        
    return mergedArray


# PATTERN LEARNED
'''
different length of arrays or empty arrays are the problem when it comes to merging sorted arrays.
So if you remove the impact of empty or shorter arrays, the problem will become easier.

if you need to use a variable for increment the index of array. And it is starting from zero. You can also consider just removing the items from zero index instead of incrementing the counter.

while merging to arrays into one, size of the merged array is going to be equal to sum of the sizes of both input arrays.
'''



# CAFE ORDER CHECKER
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    mergedArray = [0] * (len(take_out_orders) + len(dine_in_orders))

    for i in range(len(mergedArray)):
        # print(indexA, indexB, i)
        if len(take_out_orders) == 0:
            mergedArray[i] = dine_in_orders.pop(0)
        elif len(dine_in_orders) == 0:
            mergedArray[i] = take_out_orders.pop(0)
        else:
            if take_out_orders[0] <= dine_in_orders[0]:
                mergedArray[i] = take_out_orders.pop(0)
            else:
                mergedArray[i] = dine_in_orders.pop(0)

    return mergedArray == served_orders
    # return mergedArray



# PATTERN LEARNED
'''
This problem is similar to "merge sorted arrays" problem.
It's done in O(n) time and O(n) space. But since we are just suppose to return a boolean, we can do it in O(n) time and O(1) space. We don't have to create mergeArray variable. Instead of merging arrays, we can just compare them with served_orders array (which is basically a merged array) and return a boolean.

This is solution can also be done with recursion. But it will incur some extra cost in terms of memory.
'''