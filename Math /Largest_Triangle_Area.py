# Problem: Largest Triangle Area

# Method: Brute Force 

# Logic: 
         """Use three nested loops to iterate through every possible combination of three points from 
            the given list For each set of three points (x1, y1), (x2, y2), and (x3, y3), calculate
            the area of the triangle using the Shoelace formula Keep track of the maximum area found and store it in ans"""


class Solution:
    def largestTriangleArea(self, points):
        ans = 0

        for x1, y1 in points:
            for x2, y2 in points:
                for x3, y3 in points:
                    area = abs( x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
                    ans = max(ans, area)

        return ans
