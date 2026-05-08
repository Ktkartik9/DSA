# Problem: Self Dividing Numbers

# Method: Iterative Digit Validation

# Logic:
         """Loop through each number in the given range For each number
            extract its digits individually a number is "self-dividing" if 
            it contains no zeros and is divisible by every one of its digits
            if these conditions are met add the number to the results list"""

class Solution:
    def selfDividingNumbers(self, left, right): 
        ans = []

        for i in range(left , right + 1):
            temp = i
            valid = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or i % digit != 0:
                    valid = False
                    break
                temp = temp // 10
            if valid:
                ans.append(i)
        return ans
