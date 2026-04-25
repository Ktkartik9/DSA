# Problem: Binary Tree Inorder Traversal

# Method: Recursive Depth-First Search 

 # Logic: 
      """Visit the nodes in the order: Left → Root → Right
         The helper function recursively traverses the left subtree
         then processes the current root, and finally traverses the right subtree
         This traversal results in roots being visited in non-decreasing order for a Binary Search Tree"""

class Solution:
    def inorderTraversal(self, root):
        ans = []

        def inorder(root):
            if root is None:
                return 

            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        return ans 
