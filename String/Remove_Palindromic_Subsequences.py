# Problem: Remove Palindromic Subsequences

# Method: String Inversion 

Logic:
       """Since the string only contains two characters ('a' and 'b') check if s is already 
          a palindrome by comparing it to its reverse s[::-1] If it is return 1 
          because the entire string can be removed in one step Otherwise return 2 
          because all 'a's can be removed in the first step and all 'b's in the second step"""


class Solution:
    def removePalindromeSub(self, s): 

        if s == s[::-1]:
            return 1

        return 2
        
