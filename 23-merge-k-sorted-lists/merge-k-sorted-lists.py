# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # for empty lists
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                temp.append(self.merge(list1,list2))
            lists = temp
        
        return lists[0]

    def merge(self, node1, node2):
        dummy = curr = ListNode()
        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next
        
        # in case diff lengths
        curr.next = node1 or node2

        return dummy.next