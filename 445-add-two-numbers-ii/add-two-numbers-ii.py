# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse LLs, or use a stack
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry = 0
        dummy = curr = ListNode()

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 + digit2 + carry
            val, carry = total % 10, total // 10
            curr.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return self.reverse(dummy.next)
    

    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
