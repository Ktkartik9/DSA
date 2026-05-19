# Problem: Nim Game

# Method: Mathematical(Game Theory)

# Logic:
       """If the number of stones n is a multiple of 4 the first player will always lose assuming 
          both players play optimally This is because no matter how many stones (1, 2, or 3)
          the first player takes the second player can always take a number of stones that keeps
          the remainder a multiple of 4 eventually securing the last stone"""

class Solution:
    def canWinNim(self, n): 
        return n % 4 != 0
