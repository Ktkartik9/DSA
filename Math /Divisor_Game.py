# Problem: Divisor Game

# Method: Parity Check

# Logic: 
       """Alice wins if n is even because she can always force Bob into a losing position
          if n is odd Alice loses Thus it simply returns True if n % 2 == 0"""


class Solution:
    def divisorGame(self, n):
        return n % 2 == 0
        
