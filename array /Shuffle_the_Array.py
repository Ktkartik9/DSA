# Problem: Shuffle the Array

# Method: Linear Interleaving 

# Logic: 
       """Since the array is given in the form iterate from 0 to n-1
          In each step pick the element at index i 
          and the element at index i + n then append them sequentially to a new list"""

class Solution:
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])

        return ans
