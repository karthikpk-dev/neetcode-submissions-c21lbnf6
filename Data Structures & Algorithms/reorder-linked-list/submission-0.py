# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        #1.find middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #2.split second half and reverse
        second=slow.next
        slow.next=None

        prev=None
        curr=second
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        # prev = head of reversed second half
        # 3. Merge two halves
        l1,l2=head,prev
        while  l2:
            n1=l1.next
            n2=l2.next
            l1.next=l2
            l2.next=n1

            l1=n1
            l2=n2


            
