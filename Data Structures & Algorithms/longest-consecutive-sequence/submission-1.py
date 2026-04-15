class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums))==0:
            return 0
        count = set(nums)
        res=0
        for i in range(len(nums)):
            if nums[i] -1 not in count:
                j=1
                length=0
                while nums[i] + j in count:
                    length+=1
                    j+=1
                res=max(res,length)

        return res+1