# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p,c,n=head,head.next,head.next.next

        while n:
            c.next=p
            p=c
            c=n
            n=n.next
        

        head.next=None
        c.next=p
        return c

        