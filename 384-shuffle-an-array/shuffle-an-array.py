class Solution:

    def __init__(self, nums: List[int]):
        self.start = nums
        self.curr = nums[:]

    def reset(self) -> List[int]:
        self.curr = self.start[:]
        return self.curr
        

    def shuffle(self) -> List[int]:
        # Fisher–Yates algorithm: swap current element with a random one at or after it
        for i in range(len(self.curr)):
            j = random.randrange(i, len(self.curr))
            self.curr[i], self.curr[j] = self.curr[j], self.curr[i]
        return self.curr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()