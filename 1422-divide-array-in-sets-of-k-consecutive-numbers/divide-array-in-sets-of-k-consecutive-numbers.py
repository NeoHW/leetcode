class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
            
        hm = Counter(nums)

        for num in nums:
            start_num = num
            while hm[start_num - 1]:
                start_num -= 1
            
            while start_num <= num:
                while hm[start_num]:
                    for next_card in range(start_num, start_num+k):
                        if not hm[next_card]:
                            return False
                        hm[next_card] -= 1
                start_num += 1
        return True