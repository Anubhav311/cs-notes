# Hashing problem 1
def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    if len(movie_lengths) == 1:
        return (movie_lengths[0] + movie_lengths[1]) == flight_length
    
    if len(movie_lengths) < 1:
        return False
        
    movie_lengths_set = set()
    
    for i in movie_lengths:
        secondMovie = flight_length - i 
        
        if secondMovie in movie_lengths_set:
            return True
            
        movie_lengths_set.add(i)

    return False

# PATTERN LEARNED
'''
Sometimes a problem can be solved with nested loops. And sometimes the inner loop can be replaced by a set (hash table).
This will reduce the runtime from O(n^2) to O(n)

In this case, we needed to compare one item with another. So comparison can be done with a set (hash table ) also.
'''