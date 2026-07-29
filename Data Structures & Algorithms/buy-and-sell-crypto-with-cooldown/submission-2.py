class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
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