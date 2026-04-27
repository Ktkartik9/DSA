# Problem: Remove Nth Node From End of List

# Method:

# Logic: 
"""Use two pointers with a gap of 'n' nodes. 
  When the fast pointer reaches the end, the slow pointer will be just before the node to be removed"""



    def removeNthFromEnd(self, head, n):
        p1 = head
        p2 = head

        for _ in range(n):
            p2 = p2.next

        if p2 == None:
            return head.next

        while p2.next != None:
            p2 = p2.next
            p1 = p1.next

        p1.next = p1.next.next

        return head
