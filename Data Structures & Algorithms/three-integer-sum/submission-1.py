class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            tar = -nums[i]
            start,end=i+1,len(nums)-1
            while start<end:
                if nums[start]+nums[end]==tar:
                    if [nums[i],nums[start],nums[end]] not in ans:
                        ans.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                elif nums[start]+nums[end]<tar:
                    start+=1
                else:
                    end-=1
        return ans