# Problem: Best Time to Buy and Sell Stock

# Method 1: 

# Variables Explanation:
# a → minimum price 
# b → maximum profit 
# k → current profit 

class Solution(object):
    def maxProfit(self, prices):
        a = prices[0]
        b = 0

        for i in prices:
            if i < a:
                a = i
            k = i - a
            if k > b:
                b = k

        return b
