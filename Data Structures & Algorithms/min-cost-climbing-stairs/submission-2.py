class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:     
        n=len(cost)
        dp=[0]*(n+2)
        for i in range(n-1,-1,-1):

            p1=dp[i+1]
            p2=dp[i+2] if i+2<n else 0
            dp[i] = min(p1,p2) + cost[i]
            
        return min(dp[0],dp[1])