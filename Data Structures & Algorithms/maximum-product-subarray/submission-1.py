class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        min_prod=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            candidates = (nums[i],nums[i]*max_prod,nums[i]*min_prod)
            max_prod=max(candidates)
            min_prod=min(candidates)
            maxi=max(maxi,max_prod)
        return maxi
