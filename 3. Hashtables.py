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



# HASHTABLE PROBLEM TWO
def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    if len(the_string) <= 1:
        return True
    
    the_string_set = set()
    
    counter = 0
    
    for char in the_string:

        if char in the_string_set:
            counter += 1
        
        the_string_set.add(char)
    
    if counter == int(len(the_string)/2):
        return True
    
    return False


# PATTERN LEARNED
'''
Fundamental property of a palindrom is that half of it's characters are same as the other half.
If you all permutations are allowed, then you just have to confirm the existence of the character.

This problem can also be solved with "two pointers" technicque. You would have to move them once you find a similar character.

We can also solve it by checking if all characters are present even number of times. (except one character if total characters number is odd.)

Cleanest approach would be to check if it has more than one character appearing only once. If it has, it's not a palindrom.
'''


# HASHTABLE PROBLEM 3
class WordCloudData:
    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)
    def populate_words_to_counts(self, input_string):
        
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()
        current_word_start_index = 0
        current_word_length = 0
        for i, character in enumerate(input_string):
            
        # If we reached the end of the string we check if the last
        # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    
            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0
                    
            # We want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
                        
            # If the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1
                
            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    if current_word_length == 0:
                        current_word_start_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

    def add_word_to_dictionary(self, word):

        # If the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # If an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1

# PATTERN LEARNED
'''
Dictionaries are really good when it comes to keeping count of something.
Managing uppercase and lowercase words/letters is a complex problem. Spend more time on it and figure out a generic solution for future.
'''