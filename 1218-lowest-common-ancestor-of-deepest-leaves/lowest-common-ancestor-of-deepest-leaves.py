# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr):
            if not curr:
                return 0, None

            left_depth, left_lca = dfs(curr.left)
            right_depth, right_lca = dfs(curr.right)

            if left_depth > right_depth:
                return left_depth + 1, left_lca
            if left_depth < right_depth:
                return right_depth + 1, right_lca
            
            # if left_depth == right_depth, curr will be lca
            return left_depth + 1, curr
        
        return dfs(root)[1]