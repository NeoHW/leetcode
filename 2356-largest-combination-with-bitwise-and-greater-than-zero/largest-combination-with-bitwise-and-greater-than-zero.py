class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # do not have to find all possible combinations
        # intuition is for each bit position, count how many numbers have that specific bit set to 1

        ### optimising space to O(1)
        max_bit_count = 0

        for i in range(24):
            bit_count = 0
            for num in candidates:
                if (num & (1 << i)) != 0:
                    bit_count += 1
            max_bit_count = max(max_bit_count, bit_count)
        
        return max_bit_count


        '''
        bit_count = [0] * 24 # as max would be 24 bits

        for i in range(24):
            for num in candidates:
                # check if the ith bit is set
                if (num & (1 << i)) != 0:
                    bit_count[i] += 1

        return max(bit_count)
        '''