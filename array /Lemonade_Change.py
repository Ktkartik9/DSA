Problem: Lemonade Change

Method: Greedy Simulation

Logic:
         """The problem is solved by simulating the transaction process while keeping
            track of the count of $5 and $10 bills When a customer pays with $5 we simply increase the $5 count
            if they pay with $10 we must provide one $5 bill as change If they pay with $20 we prioritize giving  
            change using one $10 and one $5 bill (the greedy choice as $5 bills are more versatile)
            if a $10 bill is unavailable we attempt to use three $5 bills If neither change option is possible we return False"""

class Solution:
    def lemonadeChange(self, bills): 
        fv = 0
        tn = 0

        for i in range(0,len(bills)):
            if bills[i] == 5:
                fv += 1
            elif bills[i] == 10:
                if fv >=1:
                    fv-=1
                    tn+=1
                else:
                    return False
            elif bills[i] == 20:
                if fv >= 1 and tn >=1:
                    fv -= 1
                    tn -= 1
                elif fv >= 3:
                    fv -= 3
                else:
                    return False
                    

        return True
        
