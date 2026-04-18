class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        n=len(nums)
        sum=0
        res=float("inf")
        while j<n:
            sum+=nums[j]
            while sum>=target:
                res=min(res,j-i+1)
                sum-=nums[i]
                i+=1
            
            j+=1
        return res if res !=float("inf") else 0