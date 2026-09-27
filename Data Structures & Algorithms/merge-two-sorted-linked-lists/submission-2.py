# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    temp = list1.next
                    cur.next = list1
                    list1 = temp
                else:
                    temp = list2.next
                    cur.next = list2
                    list2 = temp
            elif list1:
                cur.next = list1
                list1 = None
            elif list2:
                cur.next = list2
                list2 = None
            
            cur = cur.next

        return dummy.next


