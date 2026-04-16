# Problem: Odd Even Linked List

# Method: Two-Pointer 
# Logic:

        """Group all odd-indexed nodes together followed by even-indexed nodes
           Use two pointers to iterate through the list linking the next pointers of odd and even
           nodes separatelyFinally"""

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even != None and even.next != None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        odd.next = even_head

        return head
