# Problem: Duplicate Zeros

# Method: Auxiliary Array Mapping

# Logic:
         """Iterate through the original array and copy each element into a temporary list temp
            Whenever a 0 is encountered append an extra 0 immediately after it Finally overwrite
            the elements of the original array arr with the first n elements from temp to maintain the fixed length"""

class Solution:
    def duplicateZeros(self, arr):
        temp = []

        for i in arr:
            temp.append(i)
            if i == 0:
                temp.append(0)
        
        for j in range(len(arr)):
            arr[j] = temp[j]
        
