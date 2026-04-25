# Problem: Delete Node in a Linked List


# Method: Value Overwriting 

# Logic:
          """Since we dont have access to the head of the list
             we cannot change the next pointer of the previous node
             we copy the value of the next node into the current node 
             then skip the next node by re-linking the current node's pointer"""


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
