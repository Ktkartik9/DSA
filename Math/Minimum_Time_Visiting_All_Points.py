# Problem: Minimum Time Visiting All Points

# Method: Chebyshev Distance Calculation

# Logic: 
       """Moving diagonally changes both x and y coordinates at the same time Thus
          the minimum time between two points is simply the larger of the two absolute
          differences: max(|x1 - x2|, |y1 - y2|) Sum this value for all consecutive pairs"""

class Solution:
    def minTimeToVisitAllPoints(self, points):
        ans = 0
        for i in range(len(points)-1):
            x1 , y1 = points[i]
            x2 , y2 = points[i+1]

            a = abs(x1 - x2)
            b = abs(y1 - y2)

            ans += max(a,b)

        return ans


