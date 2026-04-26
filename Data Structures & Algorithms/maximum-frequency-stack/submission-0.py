class FreqStack:

    def __init__(self):
        self.max_freq=0
        self.dictt= {}
        self.freq={}
        

    def push(self, val: int) -> None:
        self.freq[val]= self.freq.get(val,0)+1
        if self.freq[val] not in self.dictt:
            self.dictt[self.freq[val]]= []
        self.dictt[self.freq[val]].append(val)
        self.max_freq= max(self.max_freq,self.freq[val])
        

    def pop(self) -> int:
        x= self.dictt[self.max_freq][-1]
        self.freq[x]-=1
        self.dictt[self.max_freq].pop()
        if self.dictt[self.max_freq]==[]:
            self.max_freq-=1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()