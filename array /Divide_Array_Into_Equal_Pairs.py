# Problem: Divide Array Into Equal Pairs

# Method: Sorting & Pairwise Check

# Logic: 
      """Sort nums and compare adjacent elements in steps of 2 return False if any pair differs else True"""


class Solution:
    def divideArray(self, nums):
        nums.sort()
        for i in range(0,len(nums),2):
            if nums[i] != nums[i+1]:
                return False
        return True 
