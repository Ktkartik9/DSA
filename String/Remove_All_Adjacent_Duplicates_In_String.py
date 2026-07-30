# Problem: Remove All Adjacent Duplicates In String

# Method: Stack Data Structure

# Logic:
     """Iterate through the string character by character while maintaining a stack (list)
        If the current character matches the top element of the stack pop the top element to remove
        the adjacent duplicate Otherwise push the character onto the stack Finally join 
        all remaining elements in the stack into a result string"""


class Solution:
    def removeDuplicates(self, s):
        list1 = []

        for i in s:
            if len(list1) > 0  and list1[-1] == i:
                list1.pop()
            else:
                list1.append(i)
        ans = ''
        for j in list1:
            ans += j

        return ans

        
