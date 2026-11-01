# Problem: Largest Number

# Method: Custom String Sorting

# Logic: 
          """Convert numbers to strings sort them in descending order using a custom
             multiplier key (x * 10) to handle correct string comparisons join them
             and return '0' if the result starts with a zero"""


class Solution:
    def largestNumber(self, nums):
        
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(nums)
        return "0" if result[0] == "0" else result
