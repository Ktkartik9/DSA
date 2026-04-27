# Problem: Middle of the Linked List
# Method: Two Pointers 
# Logic: 
         """Use two pointers where the fast pointer (p1) moves twice as fast as the slow pointer (p2)
         When the fast pointer reaches the end of the list, the slow pointer will be at the middle node"""

class Solution:
    def middleNode(self, head):
        p1 = head 
        p2 = head
        
        while p1 != None and p1.next != None:
            p2 = p2.next
            p1 = p1.next.next

        return p2
