# Problem: Defanging an IP Address

# Method: Character Iteration and String Replacement

# Logic:
         """Iterate through each character in the address string If the current character is a period (.)
            append [.] to the result string ans Otherwise append the character as it is replacing every period with [.]"""


class Solution:
    def defangIPaddr(self, address):
        ans = ''

        for i in address:
            if i == '.':
                ans += '[.]' 
            else:
                ans += i

        return ans
        
