# Problem: Sum of Digits in Base K

# Method: Base Conversion via Modulo & Integer Division

# Logic: 
"""Extract digits of n in base k from right to left using the modulo 
   operator (total += n % k) then reduce n using integer division (n //= k)
   Accumulate each base-k digit into total until n becomes 0 """

class Solution:
    def sumBase(self, n, k):

        total = 0

        while n > 0:
            total += n % k
            n //= k

        return total
