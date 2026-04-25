# Problem: Binary Tree Postorder Traversal

# Method: Recursive Depth-First Search 

# Logic:
      """Visit the nodes in the order: Left → Right → Root
      The helper function recursively explores the left subtree first
      then the right subtree and finally appends the current nodes value to the result list"""

class Solution:
    def postorderTraversal(self, root):
        ans = []

        def postorder(root):
            if root is None:
                return 

            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)

        postorder(root)
        return ans 
             
        
