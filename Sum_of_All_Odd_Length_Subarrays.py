# Problem: Sum of All Odd-Length Subarrays

# Method: Brute Force 

# Logic: 
         """Use nested loops to find all possible subarrays starting at index i and ending at index j
            Keep a running sum of the subarray in current calculate its length and add current to ans 
            whenever the length is odd (length % 2 == 1)"""


class Solution:
    def sumOddLengthSubarrays(self, arr):
        ans = 0
        
        for i in range(len(arr)):
            current = 0

            for j in range(i, len(arr)):
                current += arr[j]
                length = j - i + 1
                
                if length % 2 == 1:
                    ans += current

        return ans
