# Problem: Invert Binary Tree

# Method: Recursive Depth-First Search (DFS)

# Logic: 
   """For each node swap its left and right children Recursively call the function for both 
      the left and right subtrees until all nodes have been processed If the root is None return None"""

class Solution:
    def invertTree(self, root): 
        if root is None:
            return None

        root.left , root.right = root.right , root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
