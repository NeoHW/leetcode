class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        third = 0
        second = 1
        first = 1

        for _ in range(2, n):
            curr = first+second+third
            third = second
            second = first
            first = curr
        
        return first