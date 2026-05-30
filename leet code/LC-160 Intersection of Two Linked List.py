# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1=headA
        h2=headB
        temp1,temp2=h1,h2
        count1,count2=1,1
        
        while temp1.next:
            count1+=1
            temp1=temp1.next
        while temp2.next:
            count2+=1
            temp2=temp2.next
        if temp1 is not temp2:
            return None

        if count1>count2:
            for i in range(count1-count2):
                h1=h1.next
        else:
            for i in range(count2-count1):
                h2=h2.next
        
        while h1 is not h2:
            h1=h1.next
            h2=h2.next
        return h1
        

        