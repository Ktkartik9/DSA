# Problem: Minimum Cost to Move Chips to The Same Position

# Method: Parity Counting

# Logic: 
          """Moving a chip by 2 steps costs 0 meaning all chips at even positions can be moved to position 0 for free
             and all chips at odd positions can be moved to position 1 for free Moving a chip by 1 step costs 1
             so the minimum cost to bring all chips to the same spot is simply the smaller count between the
             even positions and odd positions"""


class Solution:
    def minCostToMoveChips(self, position):
        even = 0
        odd = 0

        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)
