# Problem: Subsets 

# Method: Iterative 

# Logic: 

        """Start with an empty set in the result list
           For every number in the input array take all existing subsets in the result
           create new subsets by adding the current number 
           them and append these new subsets back into the result"""

class Solution:
    def subsets(self, nums):
        result = [[]]

        for i in nums:
            subset = []
            for j in result:
                subset.append(j+[i])
            result.extend(subset)

        return result
