# Problem: Find Lucky Integer in an Array

# Method: Linear Scan & Frequency Check

# Logic: 

        """Iterate through arr check if an element i equals its frequency (arr.count(i))
           and track the largest matching value in ans (defaulting to -1)"""


class Solution:
    def findLucky(self, arr):
        ans = -1

        for i in arr:
            if i == arr.count(i):
                if i > ans :
                    ans = i
        return ans
      
