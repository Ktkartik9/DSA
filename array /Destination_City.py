# Problem: Destination City

# Method: Hash Table 

# Logic: 
          """Collect all departure cities (i[0]) into a list des Iterate through the paths again and return
             the destination city (j[1]) that does not appear in des as the final destination city has no outgoing path"""

class Solution:
    def destCity(self, paths):
        des = []

        for i in paths:
            des.append(i[0])

        for j in paths:
            if j[1] not in des:
                return j[1] 
        
