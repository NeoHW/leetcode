class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        hm = Counter(power)
        vals = sorted(hm) # sorted list of unique power (keys)
        m = len(vals)
        dp = [0] * m    # dp[i] = best total damage ending at unique damage v_i

        j = 0           # left pointer for values < vals[i]-2
        prev_best = 0    # max(dp[0..j-1])

        for i in range(m):
            while j < i and vals[j] < vals[i] - 2:
                prev_best = max(prev_best, dp[j])
                j += 1
            dp[i] = prev_best + vals[i] * hm[vals[i]]
        
        return max(dp)