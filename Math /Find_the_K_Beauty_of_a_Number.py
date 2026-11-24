# Problem: Find the K-Beauty of a Number

# Method: Sliding Window on String & Divisibility Check

# Logic: 

        """Convert num to string s slide a window of size k across s parse each substring 
           as integer n and increment count when n is non-zero and divides num evenly"""


class Solution:
    def divisorSubstrings(self, num, k):
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            n = int(s[i:i+k])

            if n != 0 and num % n == 0:
                count += 1

        return count
