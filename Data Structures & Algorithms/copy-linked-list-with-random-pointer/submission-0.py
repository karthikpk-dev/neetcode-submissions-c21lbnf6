"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map={}
        curr=head
        while curr:
            map[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            new_node= map.get(curr)
            new_node.next=map.get(curr.next)
            new_node.random=map.get(curr.random)
            curr=curr.next
            new_node=new_node.next
        return map[head]