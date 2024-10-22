# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)

        sums = [] # min heap of k elements

        while q:
            curr_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(sums) < k:
                heapq.heappush(sums, curr_sum)
            else:
                heapq.heappushpop(sums, curr_sum)
        
        return sums[0] if len(sums) >= k else -1