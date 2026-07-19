# Problem: Sum of Encrypted Integers

# Method: String Manipulation

# Logic:
    """For each number in nums convert it to a string to find its largest digit (m)
       Create the encrypted number by repeating this maximum digit to match 
       the original numbers length (len(s)) convert it back to an integer and add it to total"""


class Solution:
    def sumOfEncryptedInt(self, nums):
        total = 0

        for i in nums:
            s = str(i)
            m = max(s)
            en = int(m * len(s))
            total += en

        return total
