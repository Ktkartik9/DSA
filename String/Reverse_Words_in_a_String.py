# Problem: Reverse Words in a String

# Method: String Splitting and Slicing

# Logic:
      """Split the input string into a list of words based on whitespace
         For each word, use slicing ([::-1]) to reverse its characters
         Append the reversed words to a list and join them back into a single string with spaces in between """

class Solution:
    def reverseWords(self,s):
        words = s.split()
        rev = []

        for i in words:
            rev.append(i[::-1])
            
        return " ".join(rev)
