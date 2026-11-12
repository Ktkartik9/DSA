# Problem: Apple Redistribution into Boxes

# Method: Greedy Approach with Sorting

# Logic: 

      """Sum total apples sort box capacities in descending order and subtract 
         the largest capacities until all apples are packed"""


class Solution:
    def minimumBoxes(self, apple, capacity):
        total = sum(apple)
        capacity.sort(reverse=True)

        count = 0

        for i in capacity:
            total -= i
            count += 1

            if total <= 0:
                break

        return count
