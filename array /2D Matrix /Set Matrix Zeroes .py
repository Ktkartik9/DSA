# Problem: Set Matrix Zeroes

# Method: Tracking Arrays 

# Logic:
"""Use two separate arrays to keep track of which rows and columns need to be zeroed 
   traverse the matrix to mark these positions
   then perform a second pass to update the matrix based on those markers"""

class Solution:
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0]) 

        row_track = [0] * r
        col_track = [0] * c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1

        for i in range(r):
            for j in range(c):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0
