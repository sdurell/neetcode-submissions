# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # following l1

        new = ListNode(0)
        dummy = new
        remainder = 0
        while (l1 or l2):
            new.next = ListNode(0)
            new = new.next
            if not l1:
                l1 = ListNode(0)
            elif not l2:
                l2 = ListNode(0)
            total = l1.val + l2.val + remainder
            remainder = total // 10
            new.val = total % 10
            l1, l2 = l1.next, l2.next
        if remainder:
            new.next = ListNode(remainder)
        
        return dummy.next
