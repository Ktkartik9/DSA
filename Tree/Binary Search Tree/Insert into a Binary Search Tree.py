# Problem: Insert into a Binary Search Tree

# Method: Iterative Insertion

# Logic:
        """Starting from the root we compare the target value with the current nodes value
           If the target is smaller we move to the left subtree; if larger, we move to the right
           We repeat this until we find an empty spot (None) 
           where the new node can be attached while maintaining the BST property"""

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], target: int):
        new_node = TreeNode(target)

        if root is None:
            return new_node
        
        curr = root
        while curr != None:
            if target < curr.val:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
            else:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break

        return root
