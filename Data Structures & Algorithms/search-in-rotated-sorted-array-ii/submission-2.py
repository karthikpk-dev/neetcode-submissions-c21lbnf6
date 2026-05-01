class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        low,high=0,n-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[low] and nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[mid]==nums[low]:
                low+=1
                continue
            if nums[mid]==nums[high]:
                high-=1
                continue
            if nums[mid]>nums[low]:
                if nums[low]<= target and nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[high]>=target and nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
        return False