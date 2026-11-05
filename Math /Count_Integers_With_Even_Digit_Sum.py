# Problem: Count Integers With Even Digit Sum

# Method: Digit Sum Iteration

# Logic: 
          """Iterate from 1 to num compute the sum of digits for each number and increment
             the count if the sum is even"""

class Solution:
    def countEven(self, num):
        count = 0

        for i in range(1, num + 1):
            total = 0
            temp = i

            while temp > 0:
                total += temp % 10
                temp //= 10

            if total % 2 == 0:
                count += 1

        return count
