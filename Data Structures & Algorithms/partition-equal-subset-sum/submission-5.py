class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n= len(nums)
        s=sum(nums)
        dp = [[False] * (s + 1) for _ in range(n + 1)]
        for i in range(s+1):
            dp[n][i]=(i == (s-i))
        for i in range(n-1,-1,-1):
            for j in range(s+1):
                not_take = dp[i + 1][j]

                take = False
                if j + nums[i] <= s:
                    take = dp[i + 1][j + nums[i]]

                dp[i][j] = take or not_take
        return dp[0][0]
        # def fun(ind,tar):
        #     if ind==n:
        #         return tar == (s-tar)
        #     if (ind, tar) in memo:
        #         return memo[(ind,tar)] 
        #     memo[(ind,tar)]=fun(ind+1,tar) or fun(ind+1,tar+nums[ind])
        #     return memo[(ind,tar)]
        # return fun(0,0)




