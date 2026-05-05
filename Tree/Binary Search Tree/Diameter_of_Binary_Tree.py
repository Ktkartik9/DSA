# Problem: Diameter of Binary Tree

# Method: Recursive Depth-First Search 

# Logic: 
    """Use a helper function to calculate the height of each node
       At every node calculate the path length passing through 
       it by summing the heights of its left and right subtrees lf + rg
       Update a global maximum variable if this path is the longest found so far
       The function returns the height of the current node to its parent"""

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0
        
        def maxDepth(node):
            nonlocal diameter
            if node is None:
                return 0
            lf = maxDepth(node.left)
            rg = maxDepth(node.right)
            
            diameter = max(diameter, lf + rg)
            return 1 + max(lf, rg)
        
        maxDepth(root)
        return diameter
