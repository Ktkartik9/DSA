# Problem: Valid Boomerang

# Method: Geometry 

# Logic:
       """Three points form a boomerang if they do not lie on a straight line 
          Instead of using division to check if the slopes are equal 
          ({y_2 - y_1}{x_2 - x_1} != {y_3 - y_1}{x_3 - x_1})
          which can cause division-by-zero errors cross multiplication is used
          If the cross products are unequal the points form a valid triangle"""

class Solution:
    def isBoomerang(self, points):
        x1 , y1 = points[0]
        x2 , y2 = points[1]
        x3 , y3 = points[2]

        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
