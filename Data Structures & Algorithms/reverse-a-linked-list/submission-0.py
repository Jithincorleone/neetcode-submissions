# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr, prev, org_next_nod= head, None, None
        
        while curr:
            org_next_node=curr.next
            curr.next=prev
            prev=curr
            curr=org_next_node

        return prev
            

        