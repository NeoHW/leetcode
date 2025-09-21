class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float('inf')] * k
        sell = [0] * k 

        for price in prices:
            buy[0] = min(buy[0], price) # cheapest first buy so far
            sell[0] = max(sell[0], price - buy[0])

            # Rounds 2..k (indexes 1..k-1): use profit from previous round as a discount
            for i in range(1, k):
                buy[i] = min(buy[i], price - sell[i-1])
                sell[i] = max(sell[i], price - buy[i])
        
        return sell[-1]
