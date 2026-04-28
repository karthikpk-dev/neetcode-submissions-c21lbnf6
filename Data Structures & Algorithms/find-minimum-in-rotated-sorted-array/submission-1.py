class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        if nums[low]<nums[high]:
            return nums[low]
        
        while low<=high:
            mid=(low+high)//2
            if (mid>0 and nums[mid-1]>nums[mid]) and (mid+1<n and nums[mid+1]>nums[mid]):
                return nums[mid]
            elif nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1
        return nums[mid]
