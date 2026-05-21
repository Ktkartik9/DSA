# Problem: Prefixes Divisible By 5

# Method: Iterative Bit-Shifting with Modulo Arithmetic

# Logic:
         """As you iterate through the binary array update the decimal value of the current prefix by shifting
            the previous value to the left (current * 2) and adding the new bit i To avoid handling excessively
            large integers apply modulo 5(% 5) at each step If the remaining value equals 0 the prefix is divisible by 5"""

class Solution:
    def prefixesDivBy5(self, nums):
        ans = []
        current = 0

        for i in nums:
            current = (current * 2 + i) % 5 
            ans.append(current==0)
        return ans
        
