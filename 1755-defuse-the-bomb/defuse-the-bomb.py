class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
        
        start, end, sum = 1, k, 0
        
        # if k < 0, start is at end of array
        if k < 0:
            start = n - abs(k)
            end = n - 1 
        
        # precompute sum of len k
        for i in range(start, end + 1):
            sum += code[i]

        for i in range(n):
            res[i] = sum
            sum -= code[(start + i) % n]
            sum += code[(end + i + 1) % n]

        return res