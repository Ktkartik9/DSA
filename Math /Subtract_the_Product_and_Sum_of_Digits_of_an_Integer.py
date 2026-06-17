# Problem: Subtract the Product and Sum of Digits of an Integer

# Method: Digit Extraction Loop

# Logic:
         """Use a while loop to extract each digit of n from right to left using modulo (n % 10)
            Multiply each digit to product add it to total (sum) and remove the last digit from n
            using integer division (n //= 10) Finally return the difference (product - total)"""


class Solution:
    def subtractProductAndSum(self, n):
        product = 1
        total = 0 

        while n > 0:
            digit = n % 10

            product *= digit
            total += digit

            n //= 10
        
        return product - total
        
