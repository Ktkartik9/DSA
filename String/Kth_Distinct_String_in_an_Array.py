# Problem: Kth Distinct String in an Array

# Method: Linear Scan & Frequency Counting

# Logic: 
            """Iterate through the array and check the frequency of each string using arr.count()
               Decrement k when a distinct string is found returning it when k reaches zero or an empty string otherwise"""


class Solution:
    def kthDistinct(self, arr, k):

        for i in arr:
            if arr.count(i) == 1:
                k -= 1
            
                if k == 0:
                    return i
        return ''
        
