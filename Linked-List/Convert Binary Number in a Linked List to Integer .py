# Problem: Convert Binary Number in a Linked List to Integer


# Method: Iterative Left Shift 


# Logic: 
        """Traverse the linked list from head to tail
           For each node multiply the current total by 2 and add the current node value
           This effectively builds the decimal representation in a single pass"""

class Solution:
    def getDecimalValue(self, head): 
        total = 0
        
        while head:
            total = 2 * total + head.val
            head = head.next
        return total
