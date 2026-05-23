# Problem: Robot Return to Origin

# Method: Coordinate Tracking Simulation

# Logic:
     """Track the robots movement on a 2D plane starting at coordinate (0, 0)
        Increment or decrement x for horizontal moves (R/L) and y for vertical moves (U/D)
        If both x and y return to 0 at the end the robot is back at the origin"""

class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0

        for i in moves:
            if i == 'R':
                x+=1
            elif i == 'L':
                x-=1
            elif i == 'U':
                y+=1
            elif i == 'D':
                y-=1
        
        return x == 0 and y == 0
