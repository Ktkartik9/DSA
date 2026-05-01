# Problem: Single Element in a Sorted Array

# Method: Bitwise XOR

# Logic:

    """XOR all elements in the array Since every number appears twice except for one
       the duplicate pairs will cancel each other out 
       leaving behind the single number""" 

class Solution:
    def singleNonDuplicate(self, nums): 
        ans = 0
        for i in nums:
            ans ^= i
        return ans
