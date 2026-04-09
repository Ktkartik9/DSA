# Problem: Valid Parentheses

# Method: Stack 


# Logic: Use a stack to track opening brackets
  every closing bracket, check if it matches the top of the stack
  If stack is empty at the end and all pairs matched, the string is valid

  class Solution:
    def isValid(self, s):
        n = len(s)
        if n % 2 == 1:
            return False
        
        stack = [] 

        for i in list(s):
            if i == '(' or i =='{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()

                if i ==')' and top != '(':
                    return False

                elif i =='}' and top != '{':
                    return False
                
                elif i ==']' and top != '[':
                    return False

        return len(stack)==0


        
