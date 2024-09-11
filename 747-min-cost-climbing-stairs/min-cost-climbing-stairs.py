class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # must reach n+1
        n = len(cost)

        if n == 2:
            return min(cost)
        
        prev, curr = cost[0], cost[1]

        for i in range(2, n):
            temp = cost[i] + min(prev, curr)
            prev = curr
            curr = temp
        
        return min(prev,curr)