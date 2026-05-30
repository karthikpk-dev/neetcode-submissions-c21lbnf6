class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        temp=[False]*n
        res=[]
        sol=[]
        def dfs(ind,temp):
            nonlocal sol,res
            if ind==n:
                res.append(sol[:])

            for i in range(n):
                if temp[i]==False:
                    sol.append(nums[i])
                    temp[i]=True
                    dfs(ind+1,temp)
                    temp[i]=False
                    sol.pop()
        dfs(0,temp)
        return res