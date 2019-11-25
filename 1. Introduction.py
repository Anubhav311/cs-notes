'''
Big O notation tells you "How quickly the runtime grows relative to the input as the input gets arbitrarily large"


N could be the actual input, or the size of input.


Drop the constant
When you are calculating the big O, you can just drop the constants. For big O notation we're looking at what happens as n get arbitrarily large. As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect.
O(2n) = O(n)


Drop the less significant terms
O(n + n^2) = O(n^2)
Again, we can get away with this because the less significant terms quickly become, well, less significant as nn gets big.


Generally, we should consider the worst case.


Space complexity
How quickly the memory usage grows relative to the input as the input gets arbitrarily large.


Big O analysis (Asymptotic analysis)
- Make a habit of thinking in time and space complexity as you design algorithms
- Big O ignores constants, but sometimes the constants matter. If we have a script that takes 5 hours to run, an optimization that divides the runtime by 5 might not affect big O, but it still saves you 4 hours of waiting.
- Beware of premature optimization. Know how to make tradeoff between time, space, readability, development time
'''