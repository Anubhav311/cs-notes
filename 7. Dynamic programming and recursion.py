# STRING PERMUTATIONS
def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[:position]
                + last_char
                + permutation_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations


# MEMOIZATION
# # O(2^n) runtime O(2^n) space
# def fib(n):
#     if n is 0 or n is 1:
#         return n

#     return fib(n-1) + fib(n-2)

# # O(2n) runtime O(2n) space
# cach = {}
# def fib(n):
#     # Compute the nth Fibonacci number
#     if n is 0 or n is 1:
#         return n

#     if n in cach:
#         return cach[n]

#     fibNum = fib(n-1) + fib(n-2)

#     cach[n] = fibNum        

#     return fibNum

# O(n) runtime and O(1) space
def fib(n):
    # Compute the nth Fibonacci number
    if n is 0 or n is 1:
        return n

    prev_prev = 0
    prev = 1
    
    for i in range(n-1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
        
    return current

