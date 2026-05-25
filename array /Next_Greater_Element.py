# Problem: Next Greater Element 

# Method: Brute Force Search

# Logic: 
         """For each element in nums1 find its matching index in nums2 From that position
            scan to the right in nums2 to find the first element that is strictly greater
            If a greater element is found, record it; otherwise, append -1 to the results"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in nums1:
            ind = nums2.index(i)
            value = -1

            for j in range(ind + 1 ,len(nums2)):
                if nums2[j] > i:
                    value = nums2[j]
                    break
            ans.append(value)
        
        return ans
