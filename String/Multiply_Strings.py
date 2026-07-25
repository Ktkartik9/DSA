# Problem: Multiply Strings

# Method: Direct Type Conversion

#Logic:
         """Convert both string inputs (num1 and num2) directly into integers using Python built-in int()
            perform the multiplication and convert the resulting product back into a string using str()"""


class Solution:
    def multiply(self,num1,num2):
        ans =int(num1) * int(num2)
        return str(ans)
        
