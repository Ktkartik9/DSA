# Problem: Remove Duplicates from Sorted Array

# Method: Two-Pointer Approach

# Logic: 
          """Track unique elements using pointer k compare each element with the previous
             one and overwrite in-place when a new unique value is found"""


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
