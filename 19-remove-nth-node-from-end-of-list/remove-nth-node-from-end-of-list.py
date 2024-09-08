# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        
        # move the fast n nodes forward
        for i in range(n):
            fast = fast.next
        
        # if this is the case, means remove the head node
        # e.g. head = [1,2], n = 2: remove node 1
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # we want to remove the next node after slow
        slow.next = slow.next.next
        
        return head