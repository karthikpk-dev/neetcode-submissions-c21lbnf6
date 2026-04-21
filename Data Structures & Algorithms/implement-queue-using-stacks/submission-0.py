class MyQueue:

    def __init__(self):
        self.inStack=deque()
        self.outStack=deque()

    def push(self, x: int) -> None:
        self.inStack.appendleft(x)

        

    def pop(self) -> int:
        if len(self.outStack)==0:
            for _ in range(len(self.inStack)):
                self.outStack.appendleft(self.inStack.popleft())
        return self.outStack.popleft()

    def peek(self) -> int:
        if len(self.outStack)==0:
            for _ in range(len(self.inStack)):
                self.outStack.appendleft(self.inStack.popleft())
        return self.outStack[0]

    def empty(self) -> bool:
        return len(self.outStack)==0 and len(self.inStack) ==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()