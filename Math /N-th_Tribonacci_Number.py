# Problem: N-th Tribonacci Number

# Method: Iterative Dynamic Programming

# Logic: 

        """Handle base cases for 0, 1, and 2, then iteratively compute subsequent values by summing
           the previous three numbers up to n"""


class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a = 0
        b = 1
        c = 1

        for i in range(3,n+1):
            d = a + b + c
            a = b
            b = c
            c = d
        return c 

       
