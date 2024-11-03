class Solution:
    def minSwaps(self, s: str) -> int:
        # count number of unpaired brackets
        stack = deque()

        for c in s:
            if not stack or c == "[":
                stack.append(c)
                continue
            
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
        
        unbalanced_pairs = len(stack) // 2
        
        # one swap can fix 2 pairs
        return (unbalanced_pairs + 1) // 2