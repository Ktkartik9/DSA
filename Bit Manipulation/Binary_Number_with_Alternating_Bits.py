# Problem: Binary Number with Alternating Bits

# Method: Bitwise Manipulation

# Logic:
  """XOR the number n with itself shifted right by one bit (n >> 1)
     If n has alternating bits this operation sets all bits in the result to 1
     Finally check if the result consists of all 1s by evaluating (n & (n + 1)) == 0"""


class Solution:
    def hasAlternatingBits(self, n):
        n ^= (n >> 1)
        return (n & (n + 1)) == 0
