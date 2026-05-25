class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x = [-1 * y for y in stones]
        heapq.heapify(x)

        while len(x) > 1:
            a=-1*heapq.heappop(x)
            b=-1*heapq.heappop(x)
            z=a-b
            if z:
                heapq.heappush(x,-1*z)
        return -1 * x[0] if len(x)==1 else 0

