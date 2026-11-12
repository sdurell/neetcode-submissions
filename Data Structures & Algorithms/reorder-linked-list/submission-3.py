# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head

        while f and f.next:
            s = s.next
            f = f.next.next

        cur = s.next
        s.next = None
        prev = temp = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        head1 = head
        head2 = prev
        while head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2

