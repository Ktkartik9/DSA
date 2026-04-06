# Linked List Cycle
# Method: 

# Logic: Use two pointers moving at different speeds. 
  If there is a cycle,the fast pointer will eventually meet the slow pointer.



    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False
