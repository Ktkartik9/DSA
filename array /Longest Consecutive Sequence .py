# Problem: Longest Consecutive Sequence

# Method:  Set 
 
class Solution:
    def longestConsecutive(self, nums):

        k = set(nums)
        longest = 0

        for i in k:
            if i - 1 not in k:
                current = i
                count = 1

                while current + 1 in k:
                    current += 1
                    count += 1

                longest = max(longest, count)
                
        return longest
        
