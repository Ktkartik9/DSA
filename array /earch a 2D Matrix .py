# Problem: Search a 2D Matrix

# Method: Linear Search 

# Logic: 
        """Iterate through each row and then each element within that row to find the target value
           Returns True if found otherwise False"""


class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for element in row:
                if element == target:
                    return True

        return False
