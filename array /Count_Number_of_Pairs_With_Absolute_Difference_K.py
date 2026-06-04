# Problem: Count Number of Pairs With Absolute Difference K

# Method: Brute Force 

# Logic: 
         """Use two nested loops to check all possible pairs (i, j) where j > i For each pair
            calculate the absolute difference between nums[i] and nums[j] if the difference equals k
            increment the count by 1"""


class Solution:
    def countKDifference(self, nums , k ):
        count = 0 

        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        
        return count 
        
