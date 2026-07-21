# Problem: Jewels and Stones

# Method: Character Matching Loop

# Logic: 
      """Loop through each character in stones and check if it exists in the jewels string
         Increment count by 1 every time a matching jewel is found then return the total count"""


class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0

        for i in stones:
            if i in jewels:
                count+=1
        return count 
        
