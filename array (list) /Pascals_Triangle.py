# Problem: Pascal's Triangle

# Method: Iterative Dynamic Programming

# Logic: 
         """Initialize a list to store the triangle For each row index i
            create a list of ones with length i + 1 For all elements except
            the first and last calculate the value by summing the two elements
            directly above it from the previous row (tri[i-1][j-1] + tri[i-1][j])
            Append each completed row to the triangle list"""

class Solution:
    def generate(self, numRows): 
        tri = []

        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
            tri.append(row)

        return tri
        
