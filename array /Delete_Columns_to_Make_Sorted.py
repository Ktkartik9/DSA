# Problem: Delete Columns to Make Sorted

# Method: Column-wise Matrix Traversal

# Logic:
          """Iterate through each column i of the grid of strings For each column check adjacent
             rows j and j-1 from top to bottom if any character is strictly smaller than
             the character directly above it (strs[j][i] < strs[j-1][i]) increment the delete
             counter and break immediately to check the next column"""

class Solution:
    def minDeletionSize(self, strs):
        row = len(strs)
        col = len(strs[0])
        length = 0

        for i in range(col):
            for j in range(1,row):
                if strs[j][i] < strs[j-1][i]:
                    length += 1

                    break
        return length 
        
        
