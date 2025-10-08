class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #sort by non-deco rder of capitals, cause i want to quickly identify what project(s) i can currently do
        s_p = sorted([(capital[i], profits[i]) for i in range(len(profits))])

        max_pq = []
        i = 0 # last unprocessed project
        while k > 0:
            while i < len(profits):
                if s_p[i][0] <= w: # i can do this proj, enough capital
                    heapq.heappush(max_pq, -s_p[i][1]) # consider (negated) profit as candidate for next proj
                else:
                    break
                i += 1
            if len(max_pq) == 0: break
            w += - heapq.heappop(max_pq)
            k -= 1
        return w