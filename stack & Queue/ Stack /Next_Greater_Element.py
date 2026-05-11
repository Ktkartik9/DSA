Problem: Next Greater Element 

Method: Stack (Reverse Iteration)

Logic: 
    """To handle the circular nature iterate through the array twice using modulo arithmetic
       Maintain a stack of elements seen so far in decreasing order For each element pop smaller
       elements from the stack; the top of the stack then represents the next greater element
       Only update the result array during the second half of the iteration """

class Solution:
    def nextGreaterElements(self, nums):
        ans = [-1] * len(nums)
        stc =[]

        for i in range(2 * len(nums)-1,-1,-1):
            while len(stc) != 0 and stc[-1] <= nums[i% len(nums)]:
                stc.pop()
            if i < len(nums):
                if len(stc) != 0:
                    ans[i] = stc[-1]
            stc.append(nums[i % len(nums)])

        return ans
