# Problem: Water Bottles

# Method: Greedy Simulation Loop

# Logic: 
          """Track total bottles drunk in t and available empty bottles in e
             both initialized to numBottles While e >= numExchange calculate 
             newly exchanged full bottles (new = e // numExchange) add them to t
             and update e with the remaining unexchanged bottles plus the newly
             emptied bottles (e % numExchange + new)"""

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        t = numBottles
        e = numBottles

        while e >= numExchange:
            new = e // numExchange
            t += new
            e = e % numExchange + new

        return t
         
