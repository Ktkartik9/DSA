# Problem: Goal Parser Interpretation

# Method: String Method Replacement

# Logic:
       """Replace every occurrence of () in the command string with "o" then replace 
          every occurrence of (al) with "al" returning the resulting interpreted string"""


class Solution:
    def interpret(self, command):
        command = command.replace("()" , "o")
        command = command.replace("(al)" , "al")

        return command
        
