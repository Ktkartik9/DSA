# Problem: Traffic Signal

# Method: Conditional Branching

# Logic: 
     """Evaluate the value of timer using conditional checks return "Green" if it equals 0
        "Orange" if it equals 30 and "Red" if it falls strictly between 30 and 90 (inclusive)
        If none of these conditions match return "Invalid"""

class Solution:
    def trafficSignal(self, timer):
        if timer == 0 :
            return "Green"
        if timer == 30:
            return  "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid"
