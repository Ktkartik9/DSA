# Problem: Maximum 69 Number

# Method: First Occurring Replacement & Re-construction

# Logic:
         """Convert num to a list of characters to change it Loop through the characters and
            replace the first '6' with a '9' to maximize the value then break out of the loop
            Finally re-construct the list back into an integer ans and return it"""


class Solution:
    def maximum69Number(self, num): 
        digits = list(str(num))
        ans = 0

        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break

        for j in digits:
            ans = ans * 10 + int(j)

        return ans
