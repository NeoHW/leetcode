class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        min_cost = float("inf")
        hm = Counter()

        for f1 in basket1:
            hm[f1] += 1
            min_cost = min(min_cost, f1)

        for f2 in basket2:
            hm[f2] -= 1
            min_cost = min(min_cost, f2)
        
        diff_list = []
        for k,v in hm.items():
            # count of indiv fruit is not even, we cannot balance it across 2 lists
            if v % 2 != 0:
                return -1
            # add the half of the imbalanced fruits as each swap fixes 2 
            diff_list.extend([k] * (abs(v) // 2))
        
        if not diff_list:
            return 0
        diff_list.sort()

        # 2 * min cost for the double swap trick
        return sum(min(2 * min_cost, x) for x in diff_list[: len(diff_list) // 2])