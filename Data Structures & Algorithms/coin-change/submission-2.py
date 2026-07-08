class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from math import inf
        
        n=len(coins)
        dp=[inf]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            ans = inf
            
            for j in range(n):
                if i>=coins[j]:
                    ans=min(1+dp[i-coins[j]],ans)
            dp[i]=ans
        return dp[amount] if dp[amount]!=inf else -1
        
        # def fun(rem):
        #     if rem==0:
        #         return 0
        #     if rem < 0:
        #         return inf
        #     if rem in memo:
        #         return memo[rem]
        #     ans=inf
            
        #     for i in range(n):
        #         ans=min(1+fun(rem-coins[i]),ans)
        #     memo[rem]=ans
        #     return ans
        
        # return fun(amount) if fun(amount)!=inf else -1
            
            