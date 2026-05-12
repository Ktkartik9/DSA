Problem: Assign Cookies

Method: Two-Pointer Greedy Approach

Logic:
       """To maximize the number of content children both the childrens greed factor
          list g and the cookie size list s are sorted in ascending order Two pointers 
          child and cookie are used to traverse the lists if the current cookies size is large
          enough to satisfy the current childs greed g[child] <= s[cookie] the child pointer and
          the count are incremented Regardless of whether the child was satisfied the cookie
          pointer is incremented to move to the next available cookie"""

class Solution:
    def findContentChildren(self, g , s):
        count = 0
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                count += 1
                child +=1
            cookie +=1

        return count
