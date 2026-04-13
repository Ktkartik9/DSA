# Problem: Palindrome Linked List


# Method: List Conversion 


# Logic: Traverse the linked list and store all node values in a list
    Compare the list with its reverse to determine if the linked list is a palindrome


    def isPalindrome(self, head):
        list=[]
        while head:
            list.append(head.val)
            head = head.next
        return list == list [::-1]

        
