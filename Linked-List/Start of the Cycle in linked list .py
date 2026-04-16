# Problem: Linked List (Find the Start of the Cycle)

# Method: Two Pointers

# Logic: 
        """detect if a cycle exists using two pointers at different speeds
           Ireset the slow pointer to the head and move both pointers one step at a time 
           The point where they meet again is the start of the cycle"""

class Solution:
    def detectCycle(self, head): 
        slow = head 
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
