# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set([0])
        self.dfs(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.seen
    
    def dfs(self, curr_node, curr_val):
        if curr_node.left:
            self.dfs(curr_node.left, 2*curr_val + 1)
            self.seen.add(2*curr_val + 1)

        if curr_node.right:
            self.dfs(curr_node.right, 2*curr_val + 2)
            self.seen.add(2*curr_val + 2)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)