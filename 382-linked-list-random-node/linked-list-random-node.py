# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    # each element should be chosen with a probability of 1/n
    def getRandom(self) -> int:
        res = None
        curr = self.head
        n = 0

        while curr:
            if random.randint(0, n) == 0:
                res = curr.val
            curr = curr.next
            n += 1 

        return res

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()