# Problem: Maximum Count of Positive Integer and Negative Integer

# Method: Linear Scan & Counter Comparison

# Logic: 

        """Count negative (n) and positive (p) integers in nums in a single pass 
           ignoring zeros and return the larger count"""


class Solution:
    def maximumCount(self, nums):
        n = 0 
        p = 0 

        for i in nums:
            if i > 0 :
                p += 1 
            elif i < 0:
                n += 1

        return max(p,n)
        
