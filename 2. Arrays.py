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
'''