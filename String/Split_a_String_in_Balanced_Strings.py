# Problem: Split a String in Balanced Strings

# Method: Greedy Balance Tracking

# Logic: 
     """Loop through each character in the string s increment balance by 1 if the character is "L" and decrement
        it by 1 if it is anything else "R" Whenever balance reaches 0 it means a balanced substring containing
        an equal number of "L" and "R" characters has been found so increment count by 1"""


class Solution:
    def balancedStringSplit(self, s): 
        balance = 0
        count = 0

        for i in s:
            if i == "L":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count

        
