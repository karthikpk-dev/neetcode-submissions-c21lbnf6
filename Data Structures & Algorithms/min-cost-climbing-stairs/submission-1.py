class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo={}
        def f(n):
            if n>=len(cost):
                return 0
            if n in memo:
                return memo[n]
            p1=f(n+1)
            p2=f(n+2)
            memo[n] = min(p1,p2) + cost[n]
            return memo[n]
        return min(f(0),f(1))