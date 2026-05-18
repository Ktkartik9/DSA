# Problem: Jump Game 

# Method: Greedy Breadth-First Search 

# Logic:
         """Maintain a window defined by left and right that represents the range of indices
            reachable within the current number of jumps For each jump find the farthest index
            that can be reached from any index within the current window Then update
            the window to start from right + 1 up to var and increment the jump count until
            the end of the array is reached"""

class Solution:
    def jump(self, nums): 
        jump = 0
        left = 0
        right = 0

        while right < len(nums)-1:
            var = 0
            for i in range(left, right+1):
                var = max(var , i+nums[i])
            left = right+1
            right = var
            jump +=1
        return jump 
        
