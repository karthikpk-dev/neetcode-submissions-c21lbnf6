class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            indx = abs(nums[i])-1
            if nums[indx] >= 0:
                nums[indx]=nums[indx]*-1
            else:
                return abs(nums[i])
        return -1