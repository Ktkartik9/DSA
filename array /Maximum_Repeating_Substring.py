# Problem: Maximum Repeating Substring

# Method: Incremental String Concatenation Simulation

# Logic: 

       """Initialize a counter k at 0 and a test substring s as word In a while loop check
          if s is present inside sequence As long as it is found increment k by 1 and append
          another copy of word to s (s += word) Return k once the repeated string is no longer a substring"""


class Solution:
    def maxRepeating(self, sequence, word):
        k = 0
        s = word
        while s in sequence:
            k += 1
            s += word

        return k


        
