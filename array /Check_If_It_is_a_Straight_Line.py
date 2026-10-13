# Problem: Check If It Is a Straight Line

# Method: Cross-Multiplication Slope Equality

# Logic: 

      """Compare the slope between the first two points and every subsequent pointusing cross-multiplication
         to prevent division by zero: (x2 - x1)(y - y1) == (y2 - y1)(x - x1) Return False if any point 
         does not satisfy the collinearity formula otherwise return True"""


class Solution:
    def checkStraightLine(self, coordinates):
        x1 , y1 = coordinates[0]
        x2 , y2 = coordinates[1]

        for i in range(2 , len(coordinates)):
            x , y = coordinates[i] 

            if (x2 - x1) * (y - y1) != (y2 - y1) * (x - x1):
                return False 
        
        return True
        
