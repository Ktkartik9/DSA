# Problem: Maximum Subarray Sum
# Given an integer array nums, find the contiguous subarray
# which has the largest sum and return its sum.

# method : Kadane’s Algorithm

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
