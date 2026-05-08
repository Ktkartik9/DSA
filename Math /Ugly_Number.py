# Problem: Ugly Number

# Method: Iterative Division 

# Logic: 
        """Check if the number is positive, as ugly numbers must be positive
           Repeatedly divide the number by 2, 3, and 5 as long as it is divisible by them
           If the final value of $n$ reduces to 1 it means the number has no prime factors other than 2, 3 or 5"""

class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        return n == 1
