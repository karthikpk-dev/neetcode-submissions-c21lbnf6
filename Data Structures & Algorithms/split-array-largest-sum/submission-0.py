class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #monotonic behaviour -> isValid(x) -> depends on x , ..... F F F T T T T .....
        def canSplit(tar):
            countSub=0
            curr_sum=0
            for x in nums:
                curr_sum+=x
                if curr_sum>tar:
                    curr_sum=x
                    countSub+=1
            return countSub+1
        low,high=max(nums),sum(nums)
        #find first valid
        while low<high:
            mid=low+(high-low)//2
            if canSplit(mid)>k:
                low=mid+1
            else:
                high=mid
        return low