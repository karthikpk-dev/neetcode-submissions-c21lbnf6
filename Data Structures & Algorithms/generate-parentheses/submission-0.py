class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]
        sol=[]
        n=n*2
        open_used,close_used=0,0

        def dfs(ind,open_used,close_used):
            if open_used==n/2 and close_used==n/2 :
                res.append("".join(sol))
                return
            if open_used<n:
                sol.append('(')
                dfs(ind+1,open_used+1,close_used)
                sol.pop()
            if close_used<open_used:
                sol.append(')')
                dfs(ind+1,open_used,close_used+1)
                sol.pop()

            
               
        dfs(0,0,0)
        return res
