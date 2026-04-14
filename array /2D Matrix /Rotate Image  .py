# Problem: Rotate Image 

# Method: Transpose and Reverse

# Logic:

"""transpose the matrix by swapping elements across the main diagonal
   reverse each row to achieve a 90-degree clockwise rotation in place """

class Solution:
    def rotate(self, matrix):
        r = len(matrix)

        for i in range(0, r - 1):
            for j in range(i + 1, r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(r):
            matrix[i].reverse()
