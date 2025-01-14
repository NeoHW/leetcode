class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count = 0
        hm = defaultdict(int)
        res = [0] * n

        for i in range(n):
            hm[A[i]] += 1
            if hm[A[i]] == 2:
                count += 1

            hm[B[i]] += 1
            if hm[B[i]] == 2:
                count += 1

            res[i] = count
        
        return res