# Problem: Distribute Elements Into Two Arrays 

# Method: Simulation & Last Element Comparison

# Logic: 
          """Initialize arr1 and arr2 with the first two elements then iterate through
             the remaining elements and append each to arr1 or arr2 based on which array
             last element is greater Return the concatenated result"""



class Solution:
    def resultArray(self, nums):

        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2,len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2


        
