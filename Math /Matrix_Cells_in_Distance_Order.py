# Problem: Matrix Cells in Distance Order

# Method: Custom Key Sorting 

# Logic:
         """Generate all possible cell coordinates [r, c] in the grid using nested loops and store them in ans
            Then sort the list using a lambda function based on their Manhattan distance to (rCenter, cCenter)
            which is calculated as |r - \text{rCenter}| + |c - \text{cCenter}|"""

class Solution:
    def allCellsDistOrder(self , rows, cols, rCenter, cCenter):
        ans = []

        for r in range(rows):
            for c in range(cols):
                ans.append([r, c])

        ans.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return ans
