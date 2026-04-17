class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                start,end=j+1,len(nums)-1
                while start<end:
                    if nums[start]+nums[end]+nums[i]+nums[j]==target:
                        if [nums[start],nums[end],nums[i],nums[j]] not in res:
                            res.append([nums[start],nums[end],nums[i],nums[j]])
                        start+=1
                        end-=1
                    elif nums[start]+nums[end]+nums[i]+nums[j]<target:
                        start+=1
                    else:
                        end-=1
        return res