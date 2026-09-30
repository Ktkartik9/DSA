# Problem: N-Repeated Element in Size 2N Array

# Method: Hash Set Lookup 

# Logic: 
   """Traverse nums while storing visited numbers in a set a
      Since only one element is repeated return the first
      number that is already found in a"""

class Solution:
    def repeatedNTimes(self, nums):
        a = set()

        for i in nums:
            if i in a:
                return i
            a.add(i)
             
        
