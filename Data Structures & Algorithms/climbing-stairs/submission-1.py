from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # iterate through list (?)
        # add 1 or 2 to total until it equals n
        # add permutation to an array, and add 1 to a total
        # after all permutations are found return total
    
        current, previous = 1,1
        for i in range(1,n):
            current,previous = current + previous, current
        return current






        

