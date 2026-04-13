# Problem: Backspace String Compare


# Method: Stack 


# Logic: Use two stacks to simulate the backspace character (#)

           #For each character
               -push it onto the stack if it's not a '#'
               -pop from the stack if it is a '#' and the stack is not empty

class Solution:
    def backspaceCompare(self, s , t ):
        s1 = []
        t1 = []

        for i in list(s):
            if i != "#" :
                s1.append(i)
            elif len(s1) > 0:
                s1.pop()

        for j in list(t):
            if j != '#':
                t1.append(j)
            elif len(t1) > 0:
                t1.pop()

        return s1 == t1

            
