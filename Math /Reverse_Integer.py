Problem: Reverse Integer

Method: Iterative Digit Extraction

Logic: 
         """Store the sign of the number and work with its absolute value
            Extract digits one by one using modulo and build the reversed
            number by multiplying the previous result by 10 After restoring
            the sign check if the reversed integer falls within the 32-bit 
            signed integer range[-2^{31},2^{31}-1] if it exceeds these bounds return 0"""

class Solution:
    def reverse(self, x):
        if x <0:
            sign = -1
        else:
            sign = 1
        x = abs(x)

        reverse = 0
        while x > 0:
            y = x%10
            reverse = reverse * 10 + y
            x = x //10
        reverse =  sign * reverse

        if reverse < -2 ** 31 or reverse > 2 ** 31 -1 :
            return 0
        return reverse

        
