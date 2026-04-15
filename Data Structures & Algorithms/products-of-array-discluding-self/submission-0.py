class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf=[],[0]*len(nums)
        pro=1
        for i in range(len(nums)):
            pro=pro * nums[i]
            pre.append(pro)
        pro=1
        for i in range(len(nums)-1,-1,-1):
            pro=pro*nums[i]
            suf[i]=pro
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i>0 and i<len(nums)-1:
                res[i]= pre[i-1]*suf[i+1]
            elif i>0:
                res[i]= pre[i-1]
            else:
                res[i]=suf[i+1]
        return res
            