class Solution:

    def __init__(self, nums: List[int]):
        self.start = nums
        self.curr = nums[:]

    def reset(self) -> List[int]:
        self.curr = self.start[:]
        return self.curr
        

    def shuffle(self) -> List[int]:
        temp = self.curr[:]

        for i in range(len(self.curr)):
            idx_to_remove = random.randrange(len(temp))
            self.curr[i] = temp.pop(idx_to_remove)

        return self.curr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()