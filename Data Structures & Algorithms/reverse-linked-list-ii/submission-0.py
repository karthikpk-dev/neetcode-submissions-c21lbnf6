# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy
        count=0
        slow,fast=None,None
        while curr:
            if count==left-1:
                slow=curr
            elif count==right:
                fast=curr.next
            count+=1
            curr=curr.next
        
        prev=fast 
        curr=slow.next
 
        sum=0
        while sum<right-left+1:
            sum+=1
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        slow.next=prev

        return dummy.next

        