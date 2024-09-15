# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse LLs, or use a stack
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None

        while stack1 or stack2 or carry:
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0

            total = digit1 + digit2 + carry
            val = total % 10
            carry = total // 10

            # instead of appending nodes m preprend them to the head of the list
            new_node = ListNode(val)
            new_node.next = head
            head = new_node

        return head