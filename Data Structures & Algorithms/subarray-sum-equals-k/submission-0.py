class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum=0
        dictt={}
        cnt=0

        for x in nums:
            pre_sum+=x
            if pre_sum==k:
                cnt+=1
            if pre_sum -k in dictt:
                cnt+=dictt[pre_sum-k]
            dictt[pre_sum] = dictt.get(pre_sum,0)+1
        return cnt