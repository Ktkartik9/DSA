# Problem: Find All Numbers Disappeared in an Array

# Method: Hash Set Lookup

# Logic:
       """The goal is to find all integers in the range [1,n] that do not appear in the given array of size n
          First the input array is converted into a set s to allow for O(1) average time complexity lookups
          The code then iterates through every integer from 1 to n if a number is not found within the set
          it is added to the result list"""

class Solution:
    def findDisappearedNumbers(self, nums):

        s = set(nums)
        result = []

        for i in range(1,len(nums)+1):
            if i not in s:
                result.append(i)

        return result 
