# Problem: Move Zeroes

# Method: Reverse Sorting

# Logic: 
        """Sort the array in reverse order to push zeros to the end """

class Solution:
    def moveZeroes(self, nums):
        nums.sort(reverse=True)
        return nums
