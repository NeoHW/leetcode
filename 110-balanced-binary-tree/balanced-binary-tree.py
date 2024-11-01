# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = [1]
        
        def heightOfSubtree(node):
            if not node:
                return 0
            
            left_height = heightOfSubtree(node.left)
            right_height = heightOfSubtree(node.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = 0

            return 1 + max(left_height, right_height)

        heightOfSubtree(root)
        return True if balanced[0] else False
        