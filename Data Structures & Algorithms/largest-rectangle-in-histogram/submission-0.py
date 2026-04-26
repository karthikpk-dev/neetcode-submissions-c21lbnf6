class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        
        lstack=[-1]*n
        rstack=[n]*n
        stack=[]
        res=0
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                lstack[i]=stack[-1]
            stack.append(i)
        stack=[]

        for i in range(n-1,-1,-1):
            while stack and heights[i] <=heights[stack[-1]]:
                stack.pop()
            if stack:
                rstack[i]=stack[-1]
            stack.append(i)
        
        for i in range(n):
            right=rstack[i]
            left=lstack[i]
            res=max(res,(right-left-1)*heights[i])
        return res