# Problem: Find First Palindromic String in the Array

# Method: String Slicing Reversal

# Logic:
       """Loop through each string i in words and check if it equals
           its reverse (i == i[::-1]) Return the first matching string 
           immediately; if no palindrome is found after checking all words return''."""


class Solution:
    def firstPalindrome(self, words):

        for i in words:
            if i == i[::-1]:
                return i
        return ''
        
