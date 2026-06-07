class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        def palindrome(start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        res=[]
        sol=[]
        def dfs(ind):
            nonlocal sol,res
            if ind==n:
                res.append(sol[:])
                return
            
            for i in range(ind,n):
                if palindrome(ind,i):
                    sol.append(s[ind:i+1])
                    dfs(i+1)
                    sol.pop()
        dfs(0)
        return res
