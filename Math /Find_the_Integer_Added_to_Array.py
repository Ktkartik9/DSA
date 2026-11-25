# Problem: Find the Integer Added to Array 

# Method: Minimum Element Difference

# Logic: 
            '''Since every element in nums1 shifts by the same integer x to form nums2
               subtracting min(nums1) from min(nums2) gives x'''


class Solution:
    def addedInteger(self, nums1, nums2):
        return min(nums2) - min(nums1)

        
