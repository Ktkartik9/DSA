# Problem: Check if The Number is Fascinating

# Method: String Concatenation & Character Sorting

# Logic: 
        """Concatenate n, n*2, and n*3, sort the resulting string characters 
           and check if it exactly equals '123456789'"""


class Solution:
    def isFascinating(self, n):

        return ''.join(sorted(str(n) + str(n * 2) + str(n * 3))) == '123456789'



# Method: Digit Extraction & Set Validation
      
# Logic: 
          """Extract digits for n, 2*n, and 3*n using divmod ensure no duplicates
             or zeros and verify all digits from 1 to 9 are present"""


class Solution:
    def isFascinating(self, n): 
        allow_set = set(range(1, 10))
        n_set = set()
        for i in range(1, 4):
            temp = n * i
            while temp:
                temp, d = divmod(temp, 10)

                if d in n_set:
                    return False
                n_set.add(d)

        return n_set == allow_set
