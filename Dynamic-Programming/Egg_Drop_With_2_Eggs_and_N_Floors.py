# Problem: Egg Drop With 2 Eggs and N Floors

# Method: Triangular Number Summation 

# Logic: 
     """With i allowed drops you can test at most 1 + 2 + \dots + i = \frac{i(i+1)}{2}
        floors by decreasing step sizes Accumulate i into ans until the total floors
        covered is at least n then return i"""


class Solution:
    def twoEggDrop(self, n):
        ans = 0
        for i in range(1,n+1):
            ans += i
            if ans >= n:
                return i
             
        
