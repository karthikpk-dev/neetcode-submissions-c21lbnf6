class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi=0
        for x in piles:
            maxi=max(maxi,x)
        low,high=1,maxi

        while low<high:
            mid=(low+high)//2
            k=0
            for i in range(len(piles)):
                k+=math.ceil(piles[i]/mid)
            if k>h:
                low=mid+1
            else:
                high=mid
        return high