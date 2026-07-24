# Problem: Replace Elements with Greatest Element on Right Side

# Method: Reverse Traversal (Optimal O(N))

# Logic: 
         """Traverse arr backwards from right to left while keeping track of the running maximum 
            (max_right starting at -1) At each step store the current element update arr[i] with max_right
            and update max_right with  max(max_right, current)"""  



class Solution:
    def replaceElements(self, arr):
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)

        return arr
