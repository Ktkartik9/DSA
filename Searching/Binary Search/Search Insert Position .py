# Problem: Search Insert Position

# Method: Binary Search 


# Logic: 
         """Use two pointers to find the target If the target is found
            the left pointer 'l' will naturally point to the correct index
            where the target should be inserted to maintain order"""


    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
