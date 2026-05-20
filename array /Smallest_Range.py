# Problem: Smallest Range 

# Method: Mathematical Optimization

# Logic:
         """To minimize the difference between the maximum and minimum values of the array decrease 
            the absolute maximum value by k and increase the absolute minimum value by k
            This reduces the overall range by 2 * k If the initial range is smaller than 2 * k
            the values can meet resulting in a minimum possible difference of 0"""



class Solution:
    def smallestRangeI(self, nums, k):
        return max(0, (max(nums) - min(nums)) - 2 * k)

        
