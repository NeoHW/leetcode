class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack of indices
        stack = deque()

        for i in range(len(prices)):
            # iterate through stack to apply discount where applicable
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack[-1]] -= prices[i]
                stack.pop()
            
            # add current index to stack
            stack.append(i)
        
        return prices