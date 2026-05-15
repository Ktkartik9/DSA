# Problem: Rotate String

# Method: Concatenation and Substring Search

# Logic: 
       """A string s can be transformed into goal via rotation only if both strings have the same length
          If they do the key observation is that all possible rotations of s are contained within the string
          formed by concatenating s with itself (s + s) By checking if goal exists as a substring in s + s
          we can determine if goal is a valid rotation of s in O(n) time"""

class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        return goal in (s + s) 
        
