# Problem: Richest Customer Wealth

# Method: Generator Expression & Built-in Max/Sum

# Logic: 
     """Calculate the total balance for each customer using sum(a) across all customer 
         account lists then return the highest total using max()"""

class Solution:
    def maximumWealth(self, accounts):
        return max(sum(a) for a in accounts) 
        
