# Problem: Sum of All Subset XOR Totals

# Method: Bitwise OR Property 

# Logic: 
           """Calculate the bitwise OR (|) of all elements in nums and store it in x
              Due to the properties of subsets each set bit in x will appear in exactly half
              (2^{n-1}) of all possible subsets Multiply x by 1 << (len(nums) - 1)
              which represents 2^{n-1} to get the final sum"""


class Solution:
    def subsetXORSum(self, nums): 
        x = 0
        for i in nums:
            x |= i

        return x * (1 << (len(nums) - 1)) 
