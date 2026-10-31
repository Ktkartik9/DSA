# Problem: Longest Palindromic Substring

# Method: Brute Force Substring Check

# Logic: 
        """Generate all possible substrings using nested loops check if each substring
           is a palindrome by comparing it to its reverse and keep track of the longest valid one"""


class Solution:
    def longestPalindrome(self, s):
        li = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                a = s[i:j+1]
                if a == a [::-1]:
                    if len(a) > len(li):
                        li = a

        return li
