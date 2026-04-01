# Problem: Product of Array Except Self
# Method: Prefix and Suffix Products
# Description:
# This method calculates the product of all elements except the current one  without using division.
  It uses two passes over the array

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
