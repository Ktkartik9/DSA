# Problem: Move Zeroes

# Method: Reverse Sorting

# Logic: 
        """Sort the array in reverse order to push zeros to the end """

class Solution:
    def moveZeroes(self, nums):
        nums.sort(reverse=True)
        return nums


# Method: Two-Pointer Swap
            
# Logic: 
            """Maintain a pointer j for the next non-zero position iterate through the array
               swapping non-zero elements with nums[j] and advancing j"""

class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i in range (len(nums)):
            if nums [i]!=0:
                nums[i], nums[j]=nums[j],nums[i]
                j+=1
