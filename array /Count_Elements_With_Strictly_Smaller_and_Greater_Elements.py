# Problem: Count Elements With Strictly Smaller and Greater Elements

# Method: Min-Max Boundary Check

# Logic:
       """The goal is to count how many elements in the array have at least one element strictly smaller 
          at least one element strictly greater than themselves By identifying the absolute smallest
          largest values in the array any element i that satisfies the condition smallest < i < largest
          is guaranteed to have elements on both sides of its value The code performs a single pass through
          the array to count these valid elements"""

class Solution:
    def countElements(self, nums):
        smallest = min(nums)
        largest = max(nums)

        count = 0 

        for i in nums:
            if smallest < i < largest:
                count += 1
        return count
