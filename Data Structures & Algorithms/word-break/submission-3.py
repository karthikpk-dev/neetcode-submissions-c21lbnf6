class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ind=0
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        for ind in range(n-1,-1,-1):
            for i in range(len(wordDict)):
                m=len(wordDict[i])
                if ind+m <= n and wordDict[i]== s[ind:ind+m]:
                    if dp[ind+m]==True:
                        dp[ind]=True
                        break
                        
            
        return dp[0]
        # def fun(ind):
        #     if ind>=n:
        #         return True
        #     if ind in memo:
        #         return memo[ind]
            
        #     for i in range(len(wordDict)):
        #         m=len(wordDict[i])
        #         if wordDict[i]== s[ind:ind+m]:
        #             if fun(ind+m)==True:
        #                 memo[ind]=True
        #                 return memo[ind]
        #     memo[ind]=False
        #     return memo[ind]
        # return fun(0)