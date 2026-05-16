# Problem: Integer Replacement

# Method: Greedy Strategy

# Logic:
       """If n is even divide it by 2 If n is odd choose the operation
          that makes the number a multiple of 4 to maximize future divisions by 2
          The only exception is n = 3 which should be decremented directly to 2"""

class Solution:
    def integerReplacement(self, n: int) -> int:
        step = 0

        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or n % 4 == 1:
                    n-=1
                else:
                    n+=1
            step+=1

        return step 



        
