# Problem: Smallest Integer Divisible by K

# Method: Modular Arithmetic 

# Logic: 
         """First check if $k$ is divisible by 2 or 5 if so no repunit  
            can be divisible by k so return -1 Otherwise iterate from length 1 up to k 
            calculating the remainder of the repunit at each step using the property pmod k
            If the remainder becomes 0 return the current length Due to the Pigeonhole
            Principle if a solution exists it must be found within k iterations"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        rem = 0
        for x in range(1,k+1):
            rem = (rem * 10 + 1) % k

            if rem == 0:
                return x

        return -1
