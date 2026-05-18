# Problem: Max Consecutive Ones 

# Method: Sliding Window 

# Logic:
        """Expand the window by moving the right pointer and tracking the number of zeros
           If the zero count exceeds k shrink the window from the left until the zero
           count is within the allowed limit The maximum window size (right - left + 1)
           encountered during the process is the result"""

class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        maximum = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maximum = max(maximum, right - left + 1)
        return maximum
