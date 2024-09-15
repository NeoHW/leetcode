# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 and l2:
            nextNumber = l1.val + l2.val + carry
            carry, value = nextNumber // 10, nextNumber % 10
            curr.next = ListNode(value)
            l1, l2 = l1.next, l2.next
            curr = curr.next
        
        while l1:
            nextNumber = l1.val + carry
            carry, value = nextNumber // 10, nextNumber % 10
            curr.next = ListNode(value)
            l1 = l1.next
            curr = curr.next

        while l2:
            nextNumber = l2.val + carry
            carry, value = nextNumber // 10, nextNumber % 10
            curr.next = ListNode(value)
            l2 = l2.next
            curr = curr.next
        
        # if there still is carry
        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next
        
