from math import inf
class Solution:
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        mini=inf
        min_sub=nums[0]
        for x in nums:
            mini=min(mini+x,x)
            min_sub=min(min_sub,mini)
        cir_max=total-min_sub
        maxi=0
        max_sub=nums[0]
        for x in nums:
            maxi=max(maxi+x,x)
            max_sub=max(max_sub,maxi)
        return max(max_sub,cir_max) if cir_max else max_sub

