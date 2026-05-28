class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)

        def fun(i,sum):
            nonlocal res,sol
            if i==n or sum>target:
                return
            if sum==target:
                res.append(sol[:])
                return

            fun(i+1,sum)
            sol.append(nums[i])
            fun(i,sum+nums[i])
            sol.pop()
        fun(0,0)
        return res