# Problem: Length of Last Word

# Method: Reverse Traversal with Early Termination

# Logic: 
        """Traverse the string s backwards from the last character to the first Skip any trailing
           spaces at the end of the string Once a non-space character is encountered increment length
           If a space is encountered after length has already started counting break out of the loop and return length"""

class Solution(object):
    def lengthOfLastWord(self, s):
        length =0

        for i in range (len(s)-1,-1,-1):
            if s[i]!=" ":
                length +=1
            elif length > 0:
                break
        return length
        
