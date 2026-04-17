class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lmax,rmax=[0]*n,[0]*n

        maxi=height[0]
        for i in range(1,n):
            
            maxi=max(maxi,height[i])
            lmax[i]=maxi
        
        maxi=height[n-1]
        for i in range(n-2,-1,-1):
            
            maxi=max(maxi,height[i])
            rmax[i]=maxi
        
        res=0

        for i in range(1,n-1):
            res+= min(lmax[i],rmax[i])-height[i]
        return res
