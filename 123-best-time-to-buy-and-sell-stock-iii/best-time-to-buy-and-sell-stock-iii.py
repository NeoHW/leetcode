class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy1: lowest price seen so far (cost of first buy)
        # sell1: best profit after first sell
        # buy2: lowest effective cost for the second buy (price - sell1)
        # sell2: best total profit after second sell
        buy1, sell1 = float('inf'), 0
        buy2, sell2 = float('inf'), 0
    
        for p in prices:
            buy1  = min(buy1, p)          # cheapest day to start (1st buy)
            sell1 = max(sell1, p - buy1)  # best profit finishing 1st transaction
            buy2  = min(buy2, p - sell1)  # cheapest effective 2nd buy (price - profit1)
            sell2 = max(sell2, p - buy2)  # best total profit finishing 2nd transaction
        
        return sell2
