class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        sol=[]
        n=len(nums)
        temp=[False]*n
        def dfs(ind,temp):
            
            if ind==n:
                res.append(sol[:])

            for i in range(n):
                if i>0 and nums[i]==nums[i-1] and temp[i-1]:
                    continue
                if temp[i]==False:
                    sol.append(nums[i])
                    temp[i]=True
                    dfs(ind+1,temp)
                    sol.pop()
                    temp[i]=False
        dfs(0,temp)
        return res