class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        hs = set(nums)
        distinct = len(hs)
        res = 0

        l = 0
        hm = defaultdict(int) 
        n = len(nums)

        for r in range(n):
            hm[nums[r]] += 1
            while len(hm) >= distinct and l <= r:
                res += (n - r)
                hm[nums[l]] -= 1
                if hm[nums[l]] == 0:
                    del hm[nums[l]]
                l += 1
        
        return res
