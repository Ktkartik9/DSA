# Problem: Find the Middle Index in Array

# Method: Prefix & Suffix Sum Balance

# Logic: 
            """Compute total sum at each index i compare left sum(ans) with right sum (total-ans-nums[i])
               returning i on equality or updating ans and returning -1 if none exists"""


class Solution:
    def findMiddleIndex(self, nums):
        total = sum(nums)
        ans = 0

        for i in range(len(nums)):
            value = total - ans - nums[i]
            if ans == value :
                return i
            ans += nums[i]
        
        return -1
