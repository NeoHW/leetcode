class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # if a number in the array is less than any number in the previous chunks, this number cannot create a new chunk
        # use a monotonic increasing stack

        stack = deque()
        for num in arr:
            if not stack or num > stack[-1]:
                # can create a new chunk if larger than all previous chunk
                stack.append(num)
            else:
                # merge all previous max largest until the new num is bigger, then push back max value of merged chunks
                max_seen = stack[-1] # as monotonic increasing
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(max_seen)
        
        return len(stack)