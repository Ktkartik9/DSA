# Problem: Longest Palindrome

# Method: Frequency Counting

# Logic: 
         """Count the frequency of each character Add the largest even part of each count
            (freq - 1 if odd) to the length If any character has an odd frequency add 1 at
            the end to place that character right in the middle of the palindrome"""

class Solution:
    def longestPalindrome(self, s):
        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        ans = 0
        odd = False

        for j in count:
            freq = count[j]

            if freq % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
                odd = True

        if odd:
            ans += 1

        return ans
