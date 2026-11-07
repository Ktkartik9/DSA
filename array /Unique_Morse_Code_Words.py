# Problem: Unique Morse Code Words

# Method: ASCII Mapping & Uniqueness Check

# Logic:
     """Map each word characters to Morse code using an array lookup accumulate 
        unique transformations and return the count"""

class Solution:
    def uniqueMorseRepresentations(self, words):

        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        
        ans = []

        for word in words:
            temp = ""

            for ch in word:
                index = ord(ch) - ord('a')
                temp += m[index]

            if temp not in ans:
                ans.append(temp)

        return len(ans)
