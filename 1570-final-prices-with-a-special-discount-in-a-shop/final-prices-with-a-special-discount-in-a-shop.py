class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack of indices
        stack = deque()

        for i, curr_price in enumerate(prices):
            # iterate through stack to apply discount where applicable
            while stack and prices[stack[-1]] >= curr_price:
                prices[stack.pop()] -= curr_price
            
            # add current index to stack
            stack.append(i)
        
        return prices