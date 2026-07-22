# Problem: Baseball Game

# Method: Stack Operations

# Logic: 
     """Maintain a stack of scores Iterate through operations for "+" add the sum of the last two scores
        for "D" append double the last score for "C" remove the last score for an integer convert and append it
        Return the sum of all remaining scores in the stack"""


class Solution:
    def calPoints(self, operations):
        stack = []

        for i in operations:
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))

        return sum(stack)
