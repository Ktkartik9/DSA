# Problem: Find All Duplicates in an Array

# Method: Hash Map Frequency Counting

# Logic: 
            """Count element frequencies using a dictionary and collect numbers appearing twice"""


class Solution:
    def findDuplicates(self, nums): 

        dic = {}
        ans = []

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for j in dic:
            if dic[j] == 2:
                ans.append(j)

        return ans
