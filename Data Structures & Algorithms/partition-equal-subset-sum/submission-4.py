class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n= len(nums)
        s=sum(nums)
        memo={}
        def fun(ind,tar):
            if ind==n:
                return tar == (s-tar)
            if (ind, tar) in memo:
                return memo[(ind,tar)] 
            memo[(ind,tar)]=fun(ind+1,tar) or fun(ind+1,tar+nums[ind])
            return memo[(ind,tar)]
        return fun(0,0)