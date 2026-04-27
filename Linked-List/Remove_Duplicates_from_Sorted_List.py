# Problem: Remove Duplicates from Sorted List

# Method: Iterative Node Deletion

# Logic: 
         """"Traverse the sorted linked list and compare each nodes value with its next node
             If the values are identical skip the next node by re-linking the current nodes pointer to the node after it
             If they are different move to the next node"""

class Solution:
    def deleteDuplicates(self, head):
        curr = head 

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
