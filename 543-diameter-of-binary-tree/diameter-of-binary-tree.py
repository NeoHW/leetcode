# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is height of left + height of right
        
        def dfs(root):
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0

            self.longest = max(self.longest, left + right) # not left + right + 1

            return 1 + max(left,right)
        

        dfs(root)
        return self.longest
