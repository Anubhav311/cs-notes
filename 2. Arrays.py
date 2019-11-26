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


