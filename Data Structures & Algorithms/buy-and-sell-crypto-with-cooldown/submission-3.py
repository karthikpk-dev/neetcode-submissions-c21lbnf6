class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        dp=[[0]*2 for _ in range(len(prices)+2)]
        for i in range(len(prices)-1,-1,-1):
            for j in range(2):
                if j:
                    dp[i][j]=max(dp[i+1][1],dp[i+1][0]-prices[i])
                else:
                    dp[i][j]=max(dp[i+2][1]+prices[i],dp[i+1][0])
        return dp[0][1]

        def fun(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy:
                memo[(i,buy)] =max (fun(i+1,True) , fun(i+1,False) - prices[i])
            else:
                memo[(i,buy)] =max( fun(i+2,True)+prices[i] ,fun(i+1,False) )
            return memo[(i,buy)]
        return fun(0,True)