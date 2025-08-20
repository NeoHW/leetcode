# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        k = len(lists)
        for i in range(k):
            if lists[i] is not None:
                heappush(pq, (lists[i].val, i))
        
        curr = dummy = ListNode()
        while pq:
            (val, idx) = heappop(pq)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx].next is not None:
                lists[idx] = lists[idx].next
                heappush(pq, (lists[idx].val, idx))
        return dummy.next