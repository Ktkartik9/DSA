# Problem: Longest Unequal Adjacent Groups Subsequence I

# Method: Greedy Linear Scan

# Logic: 
       """Start with the first word in ans Loop through the remaining indices from 1 to text{len}(words) - 1
          and greedily append words[i] whenever its group differs from the previous element's group (groups[i] != groups[i-1])"""

class Solution:
    def getLongestSubsequence(self, words, groups):
        ans = [words[0]]

        for i in range(1 , len(words)):
            if groups[i] != groups[i-1]:
                ans.append(words[i])

        return ans 
        
