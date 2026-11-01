# Problem: Longest Common Prefix

# Method: Prefix Shrinking

# Logic: 
        """Initialize prefix with the first string then iteratively shorten it by removing
           the last character until it matches the start of every remaining string in the list"""


class Solution(object):
    def longestCommonPrefix(self,str):
        if not str:
            return ""

        prefix = str[0]  
        for s in str[1:]:
        
            while not s.startswith(prefix):
                prefix = prefix[:-1]  
                if prefix == "":
                    return ""
    
        return prefix
