# Problem: Input Array Is Sorted

# Method: Two Pointers

# Logic: 
        """Use left and right pointers moving inward increment l if the sum is too small
           decrement r if too large and return 1-based indices when the target is matched"""

class Solution():
    def twoSum(self, n,t):
        l=0
        r=len(n)-1

        while l < r:
            c= n[l]+n[r]

            if c==t:
                return [l+1,r+1]
            elif c<t:
                l+=1
            else:
                r-=1
