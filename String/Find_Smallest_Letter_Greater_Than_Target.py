# Problem: Find Smallest Letter Greater Than Target

# Method: Binary Search

# Logic:  
       """The objective is to find the smallest character in a sorted list that is lexicographically
          greater than a given target Since the list is sorted a binary search approach 
          The search adjusts the left pointer to find the first character strictly greater than the target
          Because the list is considered circular the result is returned using letters[left % len(letters)]
          ensuring that if no letter is greater than the target the first letter in the list is returned"""

class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)-1

        while left <= right:
            mid = (left+right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right -= 1
        
        return letters[left % len(letters)]
        
