# Problem: Rearrange Array Elements by Sign


# Method: Two-Pointer Approach (Single Pass)

  """Logic: Initialize a result array and use two pointers 
     Traverse the input array once and place each element in its corresponding pointer location"""



    def rearrangeArray(self, nums): 
        n = len(nums)
        result = [0] * n

        pos = 0
        neg = 1

        for i in range(n):
            if nums[i] >= 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2

        return result
