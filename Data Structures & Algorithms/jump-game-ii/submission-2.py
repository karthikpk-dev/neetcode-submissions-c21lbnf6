from math import inf
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}
        def dfs(ind):
            if ind==n-1:
                return 0
            if ind>=n:
                return inf
            if ind in memo:
                return memo[ind]
            mini=inf
            for i in range(1,nums[ind]+1):
                mini=min(mini,1+dfs(ind+i))
            memo[ind]=mini
            return mini
        return dfs(0)
                