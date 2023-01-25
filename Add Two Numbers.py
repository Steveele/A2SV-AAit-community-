class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        current=node
        carry=0

        while l1 or l2 or carry:
            value1=l1.val if l1 else 0
            value2=l2.val if l2 else 0

            val=value1+value2+carry
            carry=val//10
            val=val%10
            current.next=ListNode(val)

            current=current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return node.next