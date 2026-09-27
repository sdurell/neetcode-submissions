# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = end = head
        for i in range(n):
            end = end.next
        cur = dummy
        while end:
            end = end.next
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next