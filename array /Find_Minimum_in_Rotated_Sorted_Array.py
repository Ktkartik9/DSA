# Problem: Find Minimum in Rotated Sorted Array

# Description:
# Given a rotated sorted array nums, return the minimum element.

# Approach:
- Use Binary Search
- Compare mid with right to decide the search space


class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
