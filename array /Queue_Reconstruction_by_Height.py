Problem: Queue Reconstruction by Height

Method: Greedy Placement Strategy

Logic:
       """Sort people by height from tallest to shortest and by k value ascending for ties
          Then iterate through the sorted list and insert each person into the final array at
          the index equal to their k value"""


class Solution:
    def sort_key(self, x):
        return (-x[0], x[1])

    def reconstructQueue(self, people):
        people.sort(key=self.sort_key)
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue
