# Problem: Cells with Odd Values in a Matrix

# Method: Frequency Tracking / Matrix Simulation

# Logic: 
       """Track row and column increments separately using two frequency arrays (rows and cols)
          Iterate through indices to update increment counts then check every cell (i, j) in 
          the m times n matrix if the sum of its row and column increments (rows[i] + cols[j]) 
          is odd increment the total count"""


class Solution:
    def oddCells(self, m, n, indices): 
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        count = 0

        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 == 1:
                    count += 1

        return count
