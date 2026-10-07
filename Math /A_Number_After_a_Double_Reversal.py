# Problem: A Number After a Double Reversal

# Method: String Reversal Simulation

# Logic: 
  """Reverse num by converting it to a string slicing it backwards ([::-1])
     and converting it to an integer rev1 (which strips leading zeros)
     Repeat the reversal on rev1 to produce rev2 then check if rev2 equals the original num"""

class Solution:
    def isSameAfterReversals(self, num):
        rev1 = int(str(num)[::-1])
        rev2 = int(str(rev1)[::-1])

        return rev2 == num
        
