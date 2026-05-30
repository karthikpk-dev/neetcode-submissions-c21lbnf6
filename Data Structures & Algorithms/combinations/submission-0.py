class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        sol=[]
        def dfs(ind):
            nonlocal res,sol


            if len(sol)==k:
                res.append(sol[:])
                return
            if ind>n:
                return
            
            dfs(ind+1)
            sol.append(ind)
            dfs(ind+1)
            sol.pop()
        dfs(1)
        return res