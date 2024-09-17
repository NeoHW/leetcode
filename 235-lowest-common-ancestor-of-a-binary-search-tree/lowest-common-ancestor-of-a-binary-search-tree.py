# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # search for the first value that is between p and q. That will be your lowest common ancestor
        
        while True:
            # if more than both, means ans in left subtree
            if root.val > p.val and root.val > q.val:
                root = root.left
            
            # if less than both, means ans in right subtree
            elif root.val < p.val and root.val < q.val:
                root = root.right
            
            else:
                return root