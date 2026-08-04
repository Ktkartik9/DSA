# Problem: Integer to Roman

# Method: Greedy Approach with Mapping

# Logic:
        """Define a list of Roman numeral symbols and their values sorted in descending order
           including subtractive combinations (like 900 for "CM" or 4 for "IV") Iterate through the list
           while num is greater than or equal to the current value append the corresponding Roman 
           symbol to the result string and subtract the value from num"""


class Solution:
    def intToRoman(self, num):
        roman = [
        (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        value = ''

        for i , j in roman:
            while num >= i:
                value += j
                num -= i
        
        return value

        
