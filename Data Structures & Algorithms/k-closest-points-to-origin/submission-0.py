class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        res=[]
        for i in range(len(points)):
            x=points[i]
            d = math.sqrt(x[0]**2 +x[1]**2)
            heapq.heappush(h,(d,i))
        while k>0:
            s=heapq.heappop(h)
            res.append(points[s[1]])
            k-=1
        return res
        