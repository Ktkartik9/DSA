# Problem: Fizz Buzz

# Method: Iterative Modulo Arithmetic

# Logic: 
       """Initialize an empty list answer Loop from 1 to n and check divisibility conditions
          if i is divisible by both 3 and 5 (i % 3 == 0 and i % 5 == 0) append "FizzBuzz" to answer
          if divisible only by 3 append "Fizz" if divisible only by 5 append "Buzz" otherwise
          append the string version of the number str(i) Return the completed list"""

class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
