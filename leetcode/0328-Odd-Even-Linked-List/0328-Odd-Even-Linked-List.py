# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        cur = head
        even = head.next
        cureven = even
        while cur.next:
            cureven = cur.next

            if cureven.next:
                cur.next = cureven.next
                cur = cur.next
                cureven.next = cur.next
            else:
                cureven.next = None
                break
        
        cur.next = even
        return head