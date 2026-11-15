# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        index = 0
        curr=head
        node_list=[]

        while curr:
            node_list.append(curr)
            if curr.next in node_list:
                return True
            curr=curr.next
        
        return False

        
    
    
        