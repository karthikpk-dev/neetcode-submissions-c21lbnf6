class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        sol=[]
        def dfs(ind):
            nonlocal res,sol

            res.append(sol[:])


            for i in range(ind,n):
                if i>ind and nums[i]==nums[i-1]:
                    continue

                sol.append(nums[i])
                dfs(i+1)
                sol.pop()
        dfs(0)
        return res