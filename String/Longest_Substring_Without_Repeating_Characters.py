# Problem: Longest Substring Without Repeating Characters

# Method: Sliding Window & Hash Set

# Logic: 
        """Maintain a sliding window using a set n and left pointer l while the current character s[i] is in 
           the set remove characters from the left and increment l then add s[i] and update the maximum length a"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        n = set()
        a = 0

        for i in range(len(s)):
            while s[i] in n:
                n.remove(s[l])
                l += 1
            n.add(s[i])
            a = max(a, i - l + 1)

        return a

