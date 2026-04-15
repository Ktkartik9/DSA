# Problem: Find Minimum in Rotated Sorted Array


# Method: Binary Search


# Logic: 
        """Use a modified binary search to find the pivot point
           comparing the middle element with the rightmost element
           we can determine which half of the array contains the minimum value"""

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
