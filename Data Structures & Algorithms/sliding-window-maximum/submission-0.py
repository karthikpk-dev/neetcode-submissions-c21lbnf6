class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        i,j=0,0
        n=len(nums)
        res=[]
        while j<n:
            if dq and dq[0]<= j-k:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[j]:
                dq.pop()
            dq.append(j)
            if j>=k-1:
                res.append(nums[dq[0]])
            j+=1
        return res
        