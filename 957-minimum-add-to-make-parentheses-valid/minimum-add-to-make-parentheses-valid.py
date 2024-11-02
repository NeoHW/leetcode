class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()

        for c in s:
            if not stack or c == '(':
                stack.append(c)
                continue
            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)