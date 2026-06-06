# Problem: Remove Outermost Parentheses

# Method: Balance Counter Tracking

# Logic:
         """Maintain a balance counter low to track the depth of nested parentheses
            When a  is found only add it to ans if it is not the outermost one low > 0 then increase low
            When a  is found decrease low first and only add it to ans if it is not the outermost closing partner low > 0"""



class Solution:
    def removeOuterParentheses(self, s): 
        ans = ""
        low = 0

        for i in s:
            if i == "(":
                if low > 0:
                    ans += i
                low += 1
            else:
                low -= 1
                if low > 0:
                    ans += i

        return ans
