Problem: Asteroid Collision

Method: Stack-based Simulation

Logic: 
         """Iterate through the asteroids If an asteroid is moving right
            push it onto the stack If it's moving left it will potentially
            collide with the positive asteroids already in the stack
            Use a while loop to pop smaller positive asteroids that explode
            If a collision involves asteroids of equal size both explode 
            If the stack becomes empty or contains only negative asteroids the current
            left-moving asteroid survives and is added to the stack"""

class Solution:
    def asteroidCollision(self,nums):
        stack = []

        for i in range(0,len(nums)):
            if nums[i] > 0:
                stack.append(nums[i])
            else:
                while len(stack) != 0 and stack[-1] >0 and stack[-1] < abs(nums[i]):
                    stack.pop()
                
                if len(stack) != 0 and stack[-1] == abs(nums[i]):
                    stack.pop()

                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(nums[i])
        return stack
