class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        temp = head
        stack = []
        while temp != None:
            stack.append(temp.val)
            temp = temp.next
        temp  = head 
        while len(stack) != 0:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        return True