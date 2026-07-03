class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def f(ind,can):
            if ind>=len(nums):
                return 0
            if (ind,can) in memo:
                return memo[(ind,can)]
            if can:
                res1=f(ind+1,False) + nums[ind]
                res2=f(ind+1,True)
                memo[(ind,can)]= max(res1,res2)
                return memo[(ind,can)]
            
            memo[(ind,can)]= f(ind+1,True)
            return memo[(ind,can)]
        return f(0,True)
