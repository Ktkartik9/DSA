# Problem: Merge Two Sorted Lists

# Method: Two-Pointer Iteration

# Logic: 
        """Compare values of list1 and list2 nodes append the smaller one to current.next
           advance pointers and attach any remaining nodes"""



class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

