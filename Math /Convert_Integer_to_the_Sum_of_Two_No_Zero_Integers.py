# Problem: Convert Integer to the Sum of Two No-Zero Integers

# Method: Linear Search & String Check

# Logic: 
          """Iterate through possible values of i starting from 1 up to n - 1 setting j = n - i
             Convert both numbers to strings and verify that '0' is absent from both ('0' not in str(i) and '0' not in str(j))
              Return the pair [i, j] as soon as a valid combination is found"""


class Solution:
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            j = n - i
            if '0' not in str(i) and '0' not in str(j):
                return  [i,j]        
