class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                curr_ind = nums[i]-1
                nums[curr_ind],nums[i]=nums[i],nums[curr_ind]
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i+1
        return n+1