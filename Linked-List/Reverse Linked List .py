# Given the head of a singly linked list, reverse the list and return the new head

# Approach (Iterative)
# We traverse the list and reverse the direction of each node’s next pointer.

# Initialize three pointers:
- prev = None
- curr = head
- nxt = None



class Solution:
    def reverseList(self, head):
        curr = head
        pre = None
        nxt = None

        while curr != None:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        return pre
