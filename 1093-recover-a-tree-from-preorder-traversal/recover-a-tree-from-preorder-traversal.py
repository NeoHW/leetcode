# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        index = 0
        stack = [] # this contains TreeNodes

        while index < len(traversal):
            # get depth by number of dashes
            depth = 0
            while index < len(traversal) and traversal[index] == "-":
                depth += 1
                index += 1
            
            # get value of node
            value = 0
            while index < len(traversal) and traversal[index] != "-":
                value = value * 10 + int(traversal[index])
                index += 1
            
            node = TreeNode(value)
            
            # make the stack go to the correct node using depth
            while len(stack) > depth:
                stack.pop()
            
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
            
        return stack[0]
            
