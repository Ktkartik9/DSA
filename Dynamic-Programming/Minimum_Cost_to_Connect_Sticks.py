# Problem: Minimum Cost to Connect Sticks

# Method: Mathematical Formula 

# Logic: 
"""Calculate the sum of the first n - 1 integers using the formula frac{n(n - 1)}{2}
   in O(1) time and space representing the total pairwise combinations or incremental merge costs"""

class Solution:
    def minCost(self, n):
        return n * (n-1) // 2 
        
