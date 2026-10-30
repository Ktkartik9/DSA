# Problem: Smallest Even Multiple

# Method: Conditional Parity Check

# Logic: 
        """Check if n is already even (n % 2 == 0) If it is return n since it is the smallest
           multiple of both 2 and itself otherwise multiply n by 2 to make it the smallest even multiple"""

class Solution:
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        else:
            return n * 2
