# Problem: Check if the Sentence Is Pangram

# Method: ASCII Alphabet Scan

# Logic: 
        """Check each lowercase letter 'a' through 'z' (chr(i + 97)) return False 
           if any is missing from sentence or True if all 26 appear"""



class Solution:
    def checkIfPangram(self, sentence):
        for i in range(26):
            a = chr(i+97)

            if a not in sentence :
                return False

        return True

        
