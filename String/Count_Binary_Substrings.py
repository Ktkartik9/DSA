# Problem: Count Binary Substrings

# Method: Grouping Consecutive Characters

# Logic: 
         """Count consecutive identical characters and store these counts in a list
            Then iterate through this list and add the minimum of each adjacent pair
            (min(list[i], list[i-1])) to val to get the total number of valid substrings"""

class Solution:
    def countBinarySubstrings(self, s):
        list = []
        count = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                list.append(count)
                count = 1
        
        list.append(count)
        
        val = 0

        for i in range(1 , len(list)):
            val += min(list[i] , list[i-1])
        
        return val
