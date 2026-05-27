class Solution:
    def reorganizeString(self, s: str) -> str:
        res=""
        map={}
        heap=[]
        for x in s:
            map[x]=map.get(x,0)+1
        for key,value in map.items():
            heapq.heappush(heap,(-value,key))
        if -heap[0][0] > (len(s)+1)//2:
            return ""
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            res+= first[1]+second[1]
            if -first[0]>1:
                heapq.heappush(heap,(first[0]+1,first[1]))
            if -second[0]>1:
                heapq.heappush(heap,(second[0]+1,second[1]))
        if len(heap)==1:
            res+=heap[0][1]
        return res