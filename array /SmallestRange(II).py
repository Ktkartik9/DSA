# Problem: Smallest Range 

# Method: Sorting and Greedy Linear Scan

# Logic:
       """Sort the array to establish a baseline range (nums[-1] - nums[0])
          Iterate through the array and consider a split point i where all 
          elements up to i are increased by k and all elements from i+1 
          onwards are decreased by k At each step calculate the potential
          new maximum (high) and minimum (low) values to find the minimum range configuration"""


class Solution:
    def smallestRangeII(self, nums, k):
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]

        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, high - low)

        return ans  
        
