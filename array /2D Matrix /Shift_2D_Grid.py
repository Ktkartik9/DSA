# Problem: Shift 2D Grid

# Method: 1D Index Mapping

# Logic: 
         """Convert each 2D cell (i, j) into a flat 1D index ind Shift 
            this position forward by k using modulo m * n to handle 
            the grid wrap aroundthen convert the new index back into 2D coordinates 
            (row, col) to map the element into the result grid"""

class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ind = i * n + j
                new = (ind + k) % (m * n)
                
                row = new // n
                col = new % n
                
                result[row][col] = grid[i][j]
        
        return result
