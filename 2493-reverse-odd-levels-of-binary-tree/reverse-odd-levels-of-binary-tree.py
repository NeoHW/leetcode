# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        self.__traverse_dfs(root.left, root.right, level)
        return root

    def __traverse_dfs(self, left_child, right_child, level):
        if not left_child or not right_child:
            return
        
        # current is even, means child is odd -> should reverse
        if level % 2 == 0:
            left_child.val, right_child.val = right_child.val, left_child.val
        
        # important!!
        # Perfect binary tree -> symmetrical in nature
        # to reverse, we need swap starting from the extreme ends and move inwards
        self.__traverse_dfs(left_child.left, right_child.right, level + 1)
        self.__traverse_dfs(left_child.right, right_child.left, level + 1)