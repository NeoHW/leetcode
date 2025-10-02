class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = {}

        def tri(start, end):
            if end - start <= 1:
                return 0
            
            if (start, end) in dp:
                return dp[(start, end)]

            best = float('inf')
            for k in range(start + 1, end):
                curr = tri(start, k) + tri(k, end) + values[start] * values[k] * values[end]
                best = min(best, curr)

            dp[(start, end)] = best
            return best

        return tri(0,n-1)