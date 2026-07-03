class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*2 for _ in range(n+1)]

        dp[n][0]=0
        dp[n][1]=0
        for i in range(n-1,-1,-1):
            dp[i][1]=max(dp[i+1][0]+nums[i], dp[i+1][1])
            dp[i][0]=dp[i+1][1]

        return dp[0][1]

