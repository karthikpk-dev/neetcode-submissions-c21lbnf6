class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={}
        def fun(ind):       
            if ind==n:
                return 1
            if s[ind]=='0':
                return 0
            if ind in memo:
                return memo[ind]
            #pick
            pick=0
            if ind+1<n and int(s[ind:ind+2]) <= 26:
                pick= fun(ind+2)
            #nt pick
            nt_pick=fun(ind+1)
            
            memo[ind]= nt_pick + pick 
            return memo[ind]
        return fun(0)