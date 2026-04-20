# Problem: Remove Linked List Elements

# Method: Iterative Node Deletion

# Logic: 
        """First, handle the case where the head nodes themselves contain the target value by moving the head pointer forward
          Then, traverse the list with a pointer skipping any next node that matches the target value by re-linking the current node's next pointer"""

class Solution:
    def removeElements(self, head, val): 
        while head and head.val == val:
            head = head.next

        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
