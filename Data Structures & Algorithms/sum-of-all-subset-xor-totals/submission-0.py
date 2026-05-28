class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum=0
        res=0
        n=len(nums)
        def fun(i):
            nonlocal sum , res
            if i==n:
                sum+=res
                return
            
            #not pick
            fun(i+1)

            #pick
            res^=nums[i]
            fun(i+1)
            res^=nums[i]
        fun(0)
        return sum