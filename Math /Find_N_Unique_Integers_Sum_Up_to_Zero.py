# Problem: Find N Unique Integers Sum Up to Zero

# Method: Symmetric Pair Generation

# Logic: 
           """Loop from 1 to n // 2 and append both positive and negative pairs (i and -i)
              to ans so they cancel each other out if n is odd (n % 2 == 1) simply append 0
              at the end to complete the count"""



class Solution:
    def sumZero(self, n):

        ans = []
        for i in range(1 , n//2 +1):
            ans.append(i)
            ans.append(-i)

        if n % 2 == 1:
            ans.append(0)

        return ans 

        
