# Problem: Unique Number of Occurrences

# Method: Frequency Hash Map with Set Evaluation

# Logic:
       """Count the frequency of each element using Counter Compare the number of total 
          frequency values with the number of unique frequency values (using a set)
          if both lengths are equal all occurrences are unique"""


class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)

        return len(freq.values()) == len(set(freq.values()))
