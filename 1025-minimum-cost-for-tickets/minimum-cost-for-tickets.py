class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_days = days[-1]
        dp = [0] * (max_days + 1)
        travel_days_set = set(days)

        for day in range(1, len(dp)):
            if day not in travel_days_set:
                dp[day] = dp[day-1]
            else:
                one_cost = costs[0] + dp[day-1]
                seven_cost = costs[1] + (dp[day-7] if day >= 7 else 0)
                thirty_cost = costs[2] + (dp[day-30] if day >= 30 else 0)
                dp[day] = min(one_cost, seven_cost, thirty_cost)
        
        return dp[max_days]