# Problem: Count the Digits That Divide a Number

# Method: Digit Extraction & Modulo Check

# Logic: 
            """Extract each digit of num iteratively check if it divides num evenly 
               without a remainder and increment the count if it does"""


class Solution:
    def countDigits(self, num):
        copy = num
        count = 0

        while copy > 0:
            dig = copy % 10

            if num % dig == 0:
                count +=1
            
            copy //= 10

        return count
