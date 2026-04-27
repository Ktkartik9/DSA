# Problem: Single Number

# Method: Bitwise XOR 

# Logic: 
        """Every number that appears twice will cancel itself out when XORed (a ^ a = 0)
        The number that appears only once will remain (a ^ 0 = a)
        This approach allows finding the single number without using extra space"""

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
