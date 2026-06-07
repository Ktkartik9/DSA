# Problem: Calculate Money in LeetCode Bank

# Method: Arithmetic Progression

# Logic: 
         """Use formulas to calculate the total money one part for all complete allweeks and 
            another part for the remaining extra days (re) then return their sum"""



class Solution:
    def totalMoney(self, n):
        week = n // 7
        days = n % 7

        allWeeks = 28 * week + 7 * week * (week - 1) // 2
        re = days * (week + 1) + days * (days - 1) // 2

        return allWeeks + re
