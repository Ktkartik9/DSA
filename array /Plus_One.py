# Problem: Plus One

# Method: Reverse Traversal & Carry Propagation

# Logic: 
        """Traverse digits from right to left incrementing any digit less than 9 and returning early
           If a digit is 9 set it to 0 to carry over and prepend 1 if the entire array consists of 9s"""

class Solution():   
    def plusOne(self, digits):
        n = len(digits)
    
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  
    
        return [1] + digits
