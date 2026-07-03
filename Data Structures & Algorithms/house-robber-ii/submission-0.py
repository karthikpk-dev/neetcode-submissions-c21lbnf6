class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        def f(arr):
            n=len(arr)
            dp=[[0]*2 for _ in range(n+1)]

            dp[n][0]=0
            dp[n][1]=0
            for i in range(n-1,-1,-1):
                dp[i][1]=max(dp[i+1][0]+arr[i], dp[i+1][1])
                dp[i][0]=dp[i+1][1]

            return dp[0][1]
        return max(f(nums[:-1]),f(nums[1:]))