# Problem: Min Cost Climbing Stairs

# Method: Dynamic Programming 

# Logic:
        """Iterate through the array starting from index 2 while tracking
           the minimum cost to reach the previous two steps (prev2 and prev1)
           At each step i calculate curr as the step cost plus the minimum of
           the two preceding steps Update prev2 and prev1 sequentially and return
           min(prev1, prev2) as the final minimum cost to reach the top"""

class Solution:
    def minCostClimbingStairs(self, cost):
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2,len(cost)):
            curr = cost[i] + min(prev2,prev1)
            prev2 = prev1 
            prev1 = curr

        return min(prev1,prev2)
