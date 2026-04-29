# Problem: Letter Combinations of a Phone Number

# Method: Iterative Expansion 

# Logic: 
        """Use a dictionary to map digits to letters Initialize a result list with an empty string
           For each digit in the input create a new list by taking every existing string in the result and appending 
           each letter corresponding to the current digit Update the result with this new list at each step"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dict = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        result = ['']

        for i in digits:
            subset = []
            for j in result:
                for k in dict[i]:
                    subset.append(j+k)
            result = subset
            
        return result
