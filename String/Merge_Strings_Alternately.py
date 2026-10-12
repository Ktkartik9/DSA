# Problem: Merge Strings Alternately

# Method: Single Loop Indexing

# Logic: 
       """Loop through indices from 0 up to the maximum length between word1 and word2
          At each index i append word1[i] if i is within bounds of word1 followed by word2[i]
          if i is within bounds of word2"""


class Solution:
    def mergeAlternately(self, word1, word2):
        ans =""

        for i in range(max(len(word1) , len(word2))):
            if i < len(word1):
                ans += word1[i]

            if i < len(word2):
                ans += word2[i]

        return ans 
        

