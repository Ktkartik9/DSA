# Problem: Number Complement

# Method: Binary String Manipulation

# Logic: 
      """Convert num to its binary string representation invert each bit and parse 
         the resulting string back into an integer"""

class Solution:
    def findComplement(self, num): 
        binary = bin(num)[2:]
        complement = ""

        for i in binary:
            if i == '0':
                complement += '1'
            else:
                complement += '0'

        return int(complement,2)
