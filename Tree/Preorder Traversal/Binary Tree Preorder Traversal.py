# Problem: Binary Tree Preorder Traversal

# Method: Recursive Depth-First Search (DFS)

# Logic: 
      """Visit the nodes in the order: Root → Left → Right
         We use a helper function to recursively traverse the tree
         appending the current nodes value to our list before moving to its children"""

class Solution:
    def preorderTraversal(self, root):
        ans = []
        
        def preorder(node):
            if node is None:
                return
            
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ans
