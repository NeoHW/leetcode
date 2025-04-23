class Solution:
    def countLargestGroup(self, n: int) -> int:
        hm = defaultdict(int)

        for i in range(1,n+1):
            hm[self.sumDigits(i)] += 1
        
        res = 0
        largest = 0
        for v in hm.values():
            if v == largest:
                res += 1
            elif v > largest:
                res = 1
                largest = v
        
        return res
    
    def sumDigits(self, n:int) -> int:
        res = 0
        while n != 0:
            res += n % 10
            n //= 10

        return res
