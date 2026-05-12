class DoubleListNode:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.map={}
        self.size=capacity
        self.left=DoubleListNode()
        self.right=DoubleListNode()
        self.left.next=self.right
        self.right.prev=self.left
    
    def insert(self,node: DoubleListNode):
        prev,nxt=self.right.prev,self.right 
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev
        

    def remove(self,node: DoubleListNode):
        nxt=node.next
        pre=node.prev
        nxt.prev=pre
        pre.next=nxt

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = DoubleListNode(key,value)
        self.insert(self.map[key])

        if len(self.map)>self.size:
            lru=self.left.next
            self.remove(lru)
            del self.map[lru.key]
        