# Problem: Convert the Temperature

# Method: Direct Mathematical Formula Application

# Logic:
       """Calculate Kelvin using {celsius} + 273.15 and Fahrenheit using {celsius}  1.80 + 32.00
          then return both converted values as an array [kelvin, fahrenheit]"""


class Solution:
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00

        return [kelvin, fahrenheit]
         
        
