# Problem: Minimum Bit Flips to Convert Number


# Method: Bitwise XOR and Bit Masking


# Logic: 
    """Use the XOR operator to find the bits that are different between start and goal
       iterate through the 32-bit range and use a bit mask (1 << i) to count how many of those bits are set to 1"""

class Solution:
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        count = 0
        for i in range(0, 32):
            if ans & (1 << i):
                count += 1
        return count
