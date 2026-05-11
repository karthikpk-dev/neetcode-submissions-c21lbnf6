class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyCircularQueue:
    def __init__(self, k: int):
        self.dummy=ListNode()
        self.curr=self.dummy
        self.space=k
        self.size=k


    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.curr.next=ListNode(value)
            self.curr=self.curr.next
            self.space-=1
            return True
        return False
        

    def deQueue(self) -> bool:

        if self.dummy.next:
            self.dummy.next=self.dummy.next.next
            self.space+=1
            if self.dummy.next is None:
                self.curr=self.dummy
            return True
        return False
        

    def Front(self) -> int:
        return self.dummy.next.val if self.dummy.next else -1
        

    def Rear(self) -> int:
        return self.curr.val if self.curr!=self.dummy else -1

    def isEmpty(self) -> bool:
        return self.space == self.size
        

    def isFull(self) -> bool:
        return self.space==0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()