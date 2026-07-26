class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n=len(nums)
        memo={}
        def fun(ind,prev):
            if ind==n:
                return 0
            if (ind,prev) in memo:
                return memo[(ind,prev)]
            #not take
            nt= fun(ind+1,prev)
            #take
            t=0
            if prev==-1 or  nums[prev] < nums[ind]:
                t=1+fun(ind+1,ind)
            memo[(ind,prev)]=max(nt,t)
            return memo[(ind,prev)]

            
        return fun(0,-1)