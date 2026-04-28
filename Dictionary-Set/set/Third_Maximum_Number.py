# Problem: Third Maximum Number

# Method: Set Transformation 

# Logic: 

      """Convert the array into a set to remove duplicate elements
         If the set contains fewer than three distinct numbers
         return the maximum value. Otherwise remove the first and second maximum values from the set
         the new maximum will be the original third maximum"""

class Solution:
    def thirdMax(self,nums):
        s = set(nums)

        if len(s) < 3:
            return max(s)

        s.remove(max(s))
        s.remove(max(s))

        return max(s)
