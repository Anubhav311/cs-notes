# BIG O NOTATION
'''
Big O notation tells you "How quickly the runtime grows relative to the input as the input gets arbitrarily large"


N could be the actual input, or the size of input.


Drop the constant
- When you are calculating the big O, you can just drop the constants. For big O notation we're looking at what happens as n get arbitrarily large. As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect.
O(2n) = O(n)


Drop the less significant terms
- O(n + n^2) = O(n^2)
- Again, we can get away with this because the less significant terms quickly become, well, less significant as nn gets big.


Generally, we should consider the worst case.


Space complexity
- How quickly the memory usage grows relative to the input as the input gets arbitrarily large.


Big O analysis (Asymptotic analysis)
- Make a habit of thinking in time and space complexity as you design algorithms
- Big O ignores constants, but sometimes the constants matter. If we have a script that takes 5 hours to run, an optimization that divides the runtime by 5 might not affect big O, but it still saves you 4 hours of waiting.
- Beware of premature optimization. Know how to make tradeoff between time, space, readability, development time
'''


# DATA STRUCTURES
'''
RANDOM ACCESS MEMORY
- ram <--> memory controller <--> cpu cache <--> cpu
- Computers are tuned to get an extra speed boost when reading memory addresses that are close to each other
- When the processor asks for the contents of a given memory address, the memory controller also sends the contents of a handful of nearby memory addresses.


BINARY NUMBERS
- The number system we usually use is called base 10, because each digit has ten possible values (1, 2, 3, 4, 5, 6, 7, 8, 9, and 0).
- Computers have digits with two possible values. 1 and 0.
- Base 10 is also called decimal. Base 2 is also called binary.
- The places in decimal (base 10) are sequential powers of 10. The places in binary (base 2) are sequential powers of 2.
- In hex, our possible values for each digit are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, and f. Hex numbers are often prefixed with "0x" or "#".


FIXED-WIDTH INTEGERS
- How many different numbers can we express with 1 byte (8 bits)? 2^8=256 different numbers.
- The 256 possibilities we get with 1 byte are pretty limiting. So we usually use 4 or 8 bytes (32 or 64 bits) for storing integers.
- 32-bit integers have 2^{32} possible values—more than 4 billion
- 64-bit integers have 2^{64} possible values—more than 10 billion billion (10^{19}).
- When is 32 bits not enough? When you're counting views on a viral video. YouTube famously ran into trouble when the Gangnam Style video hit over 2^{31} views, forcing them to upgrade their view counts from 32-bit to 64-bit signed integers.
- Most integers are fixed-width or fixed-length, which means the number of bits they take up doesn't change. no matter if the number is 1 or 1975248523543. It will take fixed width.
- In big O notation, we say fixed-width integers take up constant space or O(1)O(1) space.
- And because they have a constant number of bits, most simple operations on fixed-width integers (addition, subtraction, multiplication, division) take constant time (O(1)O(1) time).
- But that efficiency comes at a cost—their values are limited. Specifically, they're limited to 2^n possibilities, where n is the number of bits.


ARRAYS
- address of nth item in array = address of array start + naddress of array start+n
'''