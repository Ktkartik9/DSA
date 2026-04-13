# Problem: Valid Palindrome

# Method: Filtering and Slicing

# Logic: Filter the string to keep only alphanumeric characters and convert to lowercase.


  def isPalindrome(self, s: str) -> bool:
        str = ""
        for i in s:
            if i.isalnum():
                str += i.lower()
        return str == str[::-1]
