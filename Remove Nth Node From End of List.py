class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      leng=0
      var=head
      while var:
          var=var.next
          leng+=1
      
      
      if leng==n:
          return head.next
      leng-=n+1
      var=head
      while leng>0:
           var=var.next
           leng-=1
      var.next=var.next.next

      return head

