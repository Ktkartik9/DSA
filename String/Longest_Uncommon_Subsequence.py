# Problem: Longest Uncommon Subsequence 

# Method: String Comparison / Greedy Approach

# Logic:
        """If string a and string b are identical no uncommon subsequence exists
           so return -1 If they differ the longer string itself cannot be a subsequence 
           of the shorter string making the length of the longer string (max(len(a),len(b))) 
           the longest uncommon subsequence"""



class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        
        return max(len(a),len(b))
        
