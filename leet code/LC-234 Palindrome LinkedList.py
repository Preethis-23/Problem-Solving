# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True
        fast = head
        slow = head

        mid_prev = None
        while fast and fast.next:
            mid_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        mid_prev.next = None
        
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        left = head
        right = prev

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        