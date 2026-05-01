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
            for x in self.map[key]:
                if x[0] == timestamp:
                    return x[1]
                elif x[0]<timestamp:
                    if timestamp - x[0] < mini:
                        mini= timestamp-x[0]
                        res=x[1]
        return res
