# Problem: Day of the Year

# Method: Calendar Array & Leap Year Check

# Logic: 
    
      """Parse date into integer components year, month, and day Adjust February days in the lookup 
         list days to 29 if year is a leap year (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
         Sum the days of all preceding months (sum(days[:month - 1])) and add the current month's day"""


class Solution:
    def dayOfYear(self, date): 
        year, month, day = map(int, date.split("-"))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days[1] = 29

        return sum(days[:month - 1]) + day
