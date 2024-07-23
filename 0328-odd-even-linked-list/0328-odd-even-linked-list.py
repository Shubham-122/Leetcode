# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        o=head
        e=head.next

        while e and e.next:
            x=e.next
            e.next=e.next.next
            x.next=o.next
            o.next=x
            o=o.next
            e=e.next
        return head

        