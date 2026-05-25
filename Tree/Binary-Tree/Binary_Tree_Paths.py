Problem: Binary Tree Paths

Method: Depth-First Search 

Logic: 
      """Traverse the tree from the root down to the leaves using recursion At each node append
         its value to the current string path If a node is a leaf (has no left or right child)
         add the completed path to the ans list Otherwise append "->" and continue the traversal
         down to the left and right children"""

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []

        def dfs(node,path):
            if not node:
                return []
            path += str(node.val)
            if not node.left and not node.right:
                ans.append(path)
                return 

            dfs(node.left, path + "->")
            dfs(node.right, path + "->")
        dfs(root,"")
