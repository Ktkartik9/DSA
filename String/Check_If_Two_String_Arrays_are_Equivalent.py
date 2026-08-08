# Problem: Check If Two String Arrays are Equivalent

# Method: String Concatenation and Comparison

# Logic:
 """Iterate through word1 to concatenate all its elements into a single string s1 and do
    the same for word2 into s2 Compare s1 and s2 for equality and return True if they match otherwise False"""



class Solution:
    def arrayStringsAreEqual(self, word1, word2):        
        s1 = ''
        s2 = ''

        for i in word1:
            s1 += i
        for j in word2:
            s2 += j
        
        return s1 == s2
