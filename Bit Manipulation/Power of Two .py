# Problem: Power of Two

# Method: Iterative Power Comparison

# Logic: 
      """"Iterate through all possible powers of 2 from 0 to 31
          Check if $2^i$ equals $n$ If a match is found return True otherwise
          after checking all 32 bits return False"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0, 32):
            if 2 ** i == n:
                return True
        return False

