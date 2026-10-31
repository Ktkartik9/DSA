# Problem: Add Two Numbers

# Method: Linked List Traversal & Carry Simulation

# Logic: 
        """Traverse both linked lists simultaneously sum node values along with carry a create
           new nodes for the resulting digit and update pointers until all digits and carries are processed"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode()
        a = 0

        while l1 or l2 or a:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + a
            digit = total % 10
            a = total // 10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next
       
