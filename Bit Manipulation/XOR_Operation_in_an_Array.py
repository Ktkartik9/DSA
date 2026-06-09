# Problem: XOR Operation in an Array

# Method: Bitwise Simulation Loop

# Logic: 
           """Loop n times from i = 0 to n-1 In each iteration calculate the array 
              element using the formula start + 2 * i and update ans by performing   
              a bitwise XOR (^) with this value"""

class Solution:
    def xorOperation(self, n , start): 
        ans = 0

        for i in range(n):
            ans ^= start + 2 * i

        return ans
