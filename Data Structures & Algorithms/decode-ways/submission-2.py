class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n+1)
        dp[n]=1
        
        for ind in range(n-1,-1,-1):
            if s[ind]=='0':
                dp[ind]=0
                continue
            pick=0
            if ind+1<n and int(s[ind:ind+2]) <= 26:
                    pick= dp[ind+2]
            nt_pick=dp[ind+1]
            dp[ind]=pick+nt_pick
        return dp[0]
       