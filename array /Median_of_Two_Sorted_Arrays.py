# Problem: Median of Two Sorted Arrays

# Method: Array Concatenation & Sorting

# Logic: 
      """Combine both arrays sort the result and return the middle element for odd lengths 
          or the average of the two middle elements for even lengths"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2      
        nums.sort()              

        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])  
        else:
            return float(nums[n // 2 - 1] + nums[n // 2]) / 2
