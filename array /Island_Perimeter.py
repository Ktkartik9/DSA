# Problem: Island Perimeter

# Method: Grid Traversal and Neighbor Checking

# Logic: 
         """Iterate through the grid. For every land cell (1) initially add 4 to the perimeter
            Then look at its top neighbor (i > 0) and left neighbor (j > 0)if either neighbor is also land
            subtract 2 from the perimeter because those two cells share a boundary which removes an external edge from both"""


class Solution:
    def islandPerimeter(self, grid): 
        p = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    p += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        p -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        p -= 2

        return p
