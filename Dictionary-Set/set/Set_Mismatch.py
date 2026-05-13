Problem: Set Mismatch

Method: Hash Set Tracking

Logic: 
       """The solution identifies a duplicated and a missing number in an array
          that should contain all integers from 1 to n a set s is used to track seen numbers
          if a number is already in the set during iteration it is identified as the duplicate
          After the first pass the code iterates through the expected range [1,n] Any number
          in that range not present in the set s is identified as the missing value"""

class Solution:
    def findErrorNums(self, nums):
        dupliacte = 0
        missing = 0
        s = set()

        for i in nums:
            if i in s:
                duplicate = i
            s.add(i)

        for j in range(1,len(nums)+1):
            if j not in  s:
                missing = j

        return [duplicate , missing]

        
