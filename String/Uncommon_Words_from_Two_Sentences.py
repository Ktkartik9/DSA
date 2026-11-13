# Problem: Uncommon Words from Two Sentences

# Method: Hash Map Frequency Counting

# Logic: 

          """Combine both sentences into a single word list count frequencies using a dictionary
             and collect words that appear exactly once"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        
        word = ( s1 + ' ' + s2).split()

        count ={}
        ans =[] 

        for i in word:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1

        for j in count:
            if count[j] == 1:
                ans.append(j)

        return ans

        
