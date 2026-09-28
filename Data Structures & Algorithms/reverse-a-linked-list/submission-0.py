# Definition for singly-linked list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        res = head
        
        if head.next:
            res = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        
        return res
            
