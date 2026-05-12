# Problem: Power of Four

# Method: Iterative Division

# Logic: 
   """First ensure n is positive as powers of four must be greater than zero
      Repeatedly divide n by 4 as long as the remainder is 0 if the final value of n is 1
      it confirms that the original number was a power of four (4^k)"""

class Solution:
    def isPowerOfFour(self, n):

        if n <= 0:
            return False 
        
        while n % 4 == 0:
            n = n // 4

        if n == 1:
            return True
        return False
