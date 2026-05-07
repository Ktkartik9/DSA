# Problem: Binary Tree Maximum Path Sum

# Method: Recursive Depth-First Search 

# Logic:
        """For each node calculate the maximum gain from its left and right subtrees
           If a subtrees sum is negative treat it as 0  The current maximum path through 
           the node is the sum of its value plus both subtree gains The function returns 
           the nodes value plus the single best subtree gain to its parent as a path cannot branch twice"""

class Solution:
    def maxPathSum(self, root):
        maximum = float("-inf")

        def maximumpath(node):
            nonlocal maximum 
            if node is None:
                return 0
            ls = maximumpath(node.left)
            if ls < 0:
                ls = 0
            rs = maximumpath(node.right)
            if rs < 0:
                rs = 0
            maximum = max(maximum , ls + node.val + rs)
            return node.val + max(ls , rs) 

        maximumpath(root)
        return maximum
