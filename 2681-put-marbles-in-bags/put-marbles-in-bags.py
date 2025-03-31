class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # split into k bags -> k-1 splitting points
        # score = last weight + last weight + values of k-1 adjacent pairs

        n = len(weights)
        pair_weights = [weights[i] + weights[i+1] for i in range(n-1)]

        pair_weights.sort()

        res = 0

        # add the difference between the largest k-1 sums and smallest k-1 sums
        for i in range(k-1):
            res += pair_weights[n-2-i] - pair_weights[i]
        
        return res