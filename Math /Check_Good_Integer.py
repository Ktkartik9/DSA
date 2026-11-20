# Problem: Check Good Integer 

# Method: Digit Extraction & Sum Comparison 

# Logic: 
        """Extract each digit of n accumulate the digit sum d and squared-digit sum s
           and return True if s - d is at least 50"""


class Solution:
    def checkGoodInteger(self, n):
        s = 0
        d = 0

        while n > 0:
            dig = n % 10

            d += dig
            s += dig * dig

            n //= 10
        
        if s - d >= 50:
            return True
        else:
            return False

        
