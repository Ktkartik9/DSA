# Problem: Max Consecutive Ones

# Method: Single Pass (Counter)

# Logic: 
         """Iterate through the array while maintaining a running count of consecutive ones
            Every time a 1 is encountered increment the count and update the maximum
            if the current count is higher if a 0 is encountered reset the count to zero and continue the traversal"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maximum = 0

        for i in nums:
            if i == 1:
                count+=1
                maximum = max(maximum,count)
            else:
                count = 0

        return maximum

        
