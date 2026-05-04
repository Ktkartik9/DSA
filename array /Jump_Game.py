# Problem: Jump Game

# Method: Greedy Approach

# Logic: 
    """Maintain a variable max_ind to track the farthest index reachable at any point
       Iterate through the array if the current index i exceeds max_ind it means the end is unreachable 
       so return False otherwise update max_ind with the maximum of its current value and the potential
       jump from the current position"""


class Solution:
    def canJump(self,nums): 
        max_ind = 0 
        for i in range(0, len(nums)):
            if i > max_ind:
                return False
            max_ind = max(max_ind, i + nums[i])
        return True
