class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        r=head

        while r and r.next :
            l=l.next
            r=r.next.next
        return l


