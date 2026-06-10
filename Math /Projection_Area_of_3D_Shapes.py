# Problem: Projection Area of 3D Shapes

# Method: Grid Maxima and Non-Zero Counting

# Logic: 
           """Calculate the total area from three views: top (XY plane) front (YZ plane)
              and side (XZ plane) For the top view add 1 for every non-zero cell (grid[i][j] != 0)
              For the side view add the maximum value of each row (max(grid[i]))
              For the front view add the maximum value of each column (max(grid[j][i]))"""


class Solution:
    def projectionArea(self, grid):
        ans = 0
        n = len(grid)

        for i in range(n):
            ans += max(grid[i])  
            ans += max(grid[j][i] for j in range(n)) 

            for j in range(n):
                if grid[i][j] != 0:
                    ans += 1     

        return ans
        
