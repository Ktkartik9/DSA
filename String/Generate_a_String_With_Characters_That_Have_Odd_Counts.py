# Problem: Generate a String With Characters That Have Odd Counts

# Method: Parity-Based String Construction

# Logic:
           """Check the parity of n if n is odd return a string of n identical characters ('a' * n)
              giving one character an odd count if n is even return n - 1 copies of 'a' and one 'b'
              ensuring both characters have odd counts (n - 1 and 1)"""


class Solution:
    def generateTheString(self, n):
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'
