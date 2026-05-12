# Problem: Reverse Prefix of Word

# Method: String Slicing and Reversal

# Logic:
       """The string is divided into two segments using slicing
          The first segment includes all characters up to index k
          which is reversed using the [::-1] step operator
          This reversed prefix is then concatenated with the 
          remaining part of the string starting from index k to form the final result"""

class Solution:
    def reversePrefix(self, s , k): 
        return s[:k][::-1] + s[k:]
        
