# Problem: Valid Mountain Array

# Method: Two-Phase Linear Scan 

# Logic:
         """"Simulate climbing up and down the mountain array First use a pointer i to move forward
             as long as the elements are strictly increasing If the peak i is at the very beginning or
             the very end of the array it is not a valid mountain Finally continue moving forward  
             as long as the elements are strictly decreasing checking if the pointer successfully reaches
             the last index"""

class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        i = 0

        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1 

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1 
        
        return  i == n - 1
        
