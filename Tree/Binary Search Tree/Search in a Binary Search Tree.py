# Problem: Search in a Binary Search Tree

# Method: Iterative Search

# Logic: 
      """"Leverage the property of a BST where the left subtree contains values smaller 
          than the root and the right subtree contains values larger
          We traverse the tree using a while loop moving left if the target is smaller 
          than the current nodes value and right if it is larger until we find the node or reach a null child"""


class Solution:
    def searchBST(self, root, target):
        if root is None:
            return None

        curr = root
        while curr != None:
            if curr.val == target:
                return curr
            elif curr.val > target:
                curr = curr.left
            else:
                curr = curr.right
        
        return None
