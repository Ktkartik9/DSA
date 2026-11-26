# Problem: Base 7

# Method: Repeated Division & Remainder Prepends

# Logic: 
        """Handle 0 and negative signs separately repeatedly divide num by 7 while prepending 
           remainders to build the base-7 string and prepend '-' if num was negative"""


class Solution:
    def convertToBase7(self, num): 
        if num == 0:
            return '0'
        ans =''
        sign = ''

        if num < 0:
            sign = '-'
            num = -num

        while num > 0:
            rem = num % 7
            ans = str(rem) + ans
            num = num // 7

        return sign + ans
