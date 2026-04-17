class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=10e8
        res=0
        for x in prices:
            mini=min(x,mini)
            res=max(res,x-mini)
        return res