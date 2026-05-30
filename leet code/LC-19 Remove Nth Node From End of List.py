# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        empty=ListNode(0,head)
        movement=empty
        length=0

        while movement:
            length+=1
            movement=movement.next

        movement=empty
        steps=length-n-1
        
        for i in range(steps):
            movement=movement.next
        movement.next=movement.next.next

        return empty.next

        