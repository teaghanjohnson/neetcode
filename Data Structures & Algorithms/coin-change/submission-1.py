class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1] * (amount + 1)
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")

            if dp[amount] != -1:
                return dp[amount]

            total = float("inf")

            for coin in coins:
                cur = 1 + dfs(amount - coin)
                total = min(total, cur)
            
            dp[amount] = total
            return total
        res = dfs(amount)

        if res == float("inf"):
            return -1
        
        return res
            
