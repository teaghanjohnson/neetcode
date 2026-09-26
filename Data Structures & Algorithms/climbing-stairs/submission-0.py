from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # iterate through list (?)
        # add 1 or 2 to total until it equals n
        # add permutation to an array, and add 1 to a total
        # after all permutations are found return total
        
        memo = [-1] * n
        
        def dfs(i):
            if i >= n:
                return i == n
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dfs(i + 1) + dfs(i + 2)

            return memo[i]
        return dfs(0)






        

