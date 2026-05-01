class TimeMap:

    def __init__(self):
        self.map={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key]=[(timestamp,value)]
        else:
            self.map[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        mini=float("inf")
        res=''
        if key in self.map:
            x=self.map[key]
            low,high=0,len(self.map[key])-1
            while low<=high:
                mid=low+(high-low)//2
                if x[mid][0]<=timestamp:
                    
                    res=x[mid][1]

                    low=mid+1
                else:
                    high=mid-1
    
        return res
