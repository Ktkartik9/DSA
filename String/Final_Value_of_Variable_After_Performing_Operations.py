# Problem: Final Value of Variable After Performing Operations

# Method: Substring Search & Counter Simulation

# Logic: 
       """Initialize x to 0 and iterate through each operation string i Since every increment
          operation("++X" or "X++") contains "+" increment x by 1 if "+" is in i otherwise decrement x by 1"""


class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0 

        for i in operations:
            if "+" in i:
                x += 1
            else:
                x -= 1
        return x
        
