# Problem: Count Square Sum Triples

# Method: Brute Force / Nested Loop with Square Root Check

# Logic:
        """Iterate through all pairs (i,j) from 1 to n Compute k = \sqrt{i^2+j^2} 
           as an integer and check if k \le n and k^2 = i^2 + j^2 If valid increment the triple count"""



class Solution:
    def countTriples(self, n):
        count = 0

        for i in range(1, n + 1 ):
            for j in range(1, n + 1 ):
                k = int(( i * i + j * j ) ** 0.5)

                if k <= n and k * k == i * i + j * j:
                    count += 1

                
                
        return count

          
