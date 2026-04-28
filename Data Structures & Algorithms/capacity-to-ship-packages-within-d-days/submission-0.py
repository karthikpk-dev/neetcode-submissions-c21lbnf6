class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sums,maxi=sum(weights),max(weights)
 
        low,high=maxi,sums

        while low<high:
            mid=(low+high)//2

            i=0
            val=mid
            k=0
            while i<len(weights):
                while i<len(weights) and val-weights[i]>=0:
                    
                    val-=weights[i]
                    i+=1
                val=mid
                k+=1
            if k>days:
                low=mid+1
            else:
                high=mid
        return low