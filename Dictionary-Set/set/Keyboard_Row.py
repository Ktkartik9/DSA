# Problem: Keyboard Row

# Method: Set Subset Comparison

# Logic:
       """Define each keyboard row as a set of lowercase characters Convert each word to a lowercase
          set and check if it is a subset (<=) of any single row (r1, r2, or r3) Append words
          that fit entirely within one row to answer"""



class Solution:
    def findWords(self, words):
        r1 = set("qwertyuiop") 
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")

        answer = []

        for i in words:
            word = set(i.lower())

            if word <= r1 or word <= r2 or word <= r3:
                answer.append(i)

        return answer
