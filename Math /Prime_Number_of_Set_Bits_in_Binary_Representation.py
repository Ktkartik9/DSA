# Problem: Prime Number of Set Bits in Binary Representation

# Method: Bit Manipulation and Set Lookup

# Logic: 
         """Loop through each number from left to right and count its set bits (1s) using bitwise operations
            if the total number of bits is a prime number present in the pre-defined primes set increment ans by 1"""

class Solution:
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0

        for i in range(left, right + 1):
            bits = 0
            n = i

            while n > 0:
                bits += n & 1
                n >>= 1

            if bits in primes:
                ans += 1

        return ans
