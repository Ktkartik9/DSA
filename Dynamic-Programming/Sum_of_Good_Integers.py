# Problem: Sum of Good Integers 

# Method: Linear Range Scan & Bitwise Filtering

# Logic: 
         """Iterate through integers x within a bounded range defined around n and k
            Check whether each integer satisfies the range condition and whether its bitwise AND
            with n evaluates to zero((n & x)== 0) Accumulate such values into total and return the final sum"""


class Solution:
    def sumOfGoodIntegers(self, n, k): 
        total = 0

        for x in range(1, n + k + 1):
            if n - k <= x <= n + k:
                if (n & x) == 0:
                    total += x

        return total
