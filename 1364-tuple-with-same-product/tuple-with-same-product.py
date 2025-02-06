class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # each unique 4 numbers combination will have 8 total combinations 
        hm = defaultdict(int)
        res = 0
    
        # count how many times each product appears
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                hm[nums[i] * nums[j]] += 1
        
        for product_freq in hm.values():
            # this is nC2 (number of ways to choose 2 pairs from n pairs)
            pairs_of_equal_product = (product_freq * (product_freq - 1) // 2)
            res += pairs_of_equal_product * 8
        
        return res