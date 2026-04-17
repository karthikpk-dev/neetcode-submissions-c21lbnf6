class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        start,end=0,n-1
        res=0
        while start<end:
            res= max(res,min(heights[start],heights[end])*(end-start))
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return res


