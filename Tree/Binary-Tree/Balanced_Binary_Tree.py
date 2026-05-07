# Problem: Balanced Binary Tree

# Method: Recursive DFS (Height-balanced check)

# Logic: 
        """Use a helper function to calculate the height of each node
           If any subtree is found to be unbalanced  return -1 to signal a failure
           The function propagates this -1 upward otherwise it returns the actual height of the node"""

class Solution:
    def isBalanced(self, root):

        def balanced(node):
            if node is None:
                return 0
            ls = balanced(node.left)
            if ls == -1:
                return -1
            rs = balanced(node.right)
            if rs == -1:
                return -1
            if abs(ls - rs) > 1:
                return -1
            return 1 + max(ls,rs)

        x = balanced(root)
        if x == -1:
            return False
        else:
            return True 

