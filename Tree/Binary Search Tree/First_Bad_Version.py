# Problem: First Bad Version

# Method: Binary Search

# Logic:
         """Use binary search to minimize API calls If the midpoint mid is a bad version
            the first bad version must be at mid or to its left so set right = mid
            If mid is not a bad version the first bad version must be to its right so set left = mid + 1
            The loop terminates when left and right meet at the first bad version"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):     #pre-define 
                right = mid
            else:
                left = mid + 1

        return left
