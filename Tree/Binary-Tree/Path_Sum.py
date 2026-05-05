# Problem: Path Sum

# Method: Recursive Depth-First Search 

# Logic:
         """Traverse the tree while subtracting the current nodes value from the targetsum
            If a leaf node is reached check if the remaining targetsum equals the leaf nodes value
            Return True if either the left or right subtree path satisfies the condition"""

class Solution:
    def hasPathSum(self, root , targetsum) : 
        if root is None:
            return False
        if root.left is None and root.right is None:
            return  targetsum == root.val
        
        return (self.hasPathSum(root.left, targetsum - root.val)or
        self.hasPathSum(root.right, targetsum - root.val)
        )

  
