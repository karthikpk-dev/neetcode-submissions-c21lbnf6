class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        res=[]
        for i in range(len(arr)):
            heapq.heappush(heap,(abs(x-arr[i]),arr[i]))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        res.sort()
        return res