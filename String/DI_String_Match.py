# Problem: DI String Match

# Method: Two-Pointer / Greedy Approach

# Logic:
       """Maintain low at 0 and high at len(s) Iterate through string s: if 'I'
          append low and increment it if 'D' append high and decrement it Finally
          append the remaining value (low or high) to complete the array"""


class Solution:
    def diStringMatch(self, s):
        low = 0
        high = len(s)
        ans = []

        for i in s:
            if i == 'I':
                ans.append(low)
                low += 1

            else:
                ans.append(high)
                high -= 1

        ans.append(low)
        return ans

        
